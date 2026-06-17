from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from preprocessor import (
    preprocess_with_spacy,
    extract_skills_from_text,
    extract_skills_with_implied,
    extract_email,
    extract_phone,
    extract_experience_years,
    extract_name_from_text,
    get_experience_label
)


def calculate_tfidf_score(job_description, resume_text):
    """Calculate TF-IDF cosine similarity"""
    
    processed_job = preprocess_with_spacy(job_description)
    processed_resume = preprocess_with_spacy(resume_text)
    
    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        max_features=5000,
        sublinear_tf=True
    )
    
    try:
        tfidf_matrix = vectorizer.fit_transform([processed_job, processed_resume])
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
        score = float(similarity[0][0]) * 100
        score = min(score * 2.5, 100)
    except Exception as e:
        print(f"TF-IDF Error: {e}")
        score = 0
    
    return round(score, 2)


def calculate_skills_match_score(job_description, resume_text):
    """Calculate skills matching score with implied skills"""
    
    job_skills = extract_skills_from_text(job_description)
    resume_skills = extract_skills_with_implied(resume_text)
    
    if not job_skills:
        return 0, [], [], resume_skills
    
    matched_skills = [skill for skill in job_skills if skill in resume_skills]
    missing_skills = [skill for skill in job_skills if skill not in resume_skills]
    
    score = (len(matched_skills) / len(job_skills)) * 100
    
    return round(score, 2), matched_skills, missing_skills, resume_skills


def calculate_keyword_score(job_description, resume_text):
    """Calculate keyword matching"""
    
    job_words = set(job_description.lower().split())
    resume_words = set(resume_text.lower().split())
    
    stop_words = {
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to',
        'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be',
        'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
        'should', 'could', 'may', 'might', 'must', 'shall', 'can',
        'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she',
        'it', 'we', 'they', 'them', 'their', 'our', 'your', 'my',
        'from', 'as', 'if', 'than', 'so', 'into', 'about', 'through',
        '•', '-', '—'
    }
    
    job_keywords = {w for w in job_words if w not in stop_words and len(w) > 2}
    resume_keywords = {w for w in resume_words if w not in stop_words and len(w) > 2}
    
    if not job_keywords:
        return 0
    
    matched = job_keywords.intersection(resume_keywords)
    score = (len(matched) / len(job_keywords)) * 100
    
    return round(score, 2)


def rank_resumes(job_description, resumes):
    """Main ranking function"""
    
    ranked_results = []
    
    for resume in resumes:
        resume_text = resume['text']
        
        # Calculate all scores
        tfidf_score = calculate_tfidf_score(job_description, resume_text)
        
        skills_score, matched_skills, missing_skills, all_resume_skills = calculate_skills_match_score(
            job_description, resume_text
        )
        
        keyword_score = calculate_keyword_score(job_description, resume_text)
        
        # 🎯 NEW WEIGHTED SCORE - Skills weighted highest
        final_score = (
            (tfidf_score * 0.15) +     # 15% - text similarity
            (skills_score * 0.70) +    # 70% - skills (most important!)
            (keyword_score * 0.15)     # 15% - keyword match
        )
        
        # Get better name
        better_name = extract_name_from_text(resume_text)
        display_name = better_name if better_name else resume['name']
        
        # Get experience
        experience = extract_experience_years(resume_text)
        
        candidate = {
            'name': display_name,
            'filename': resume['filename'],
            'email': extract_email(resume_text),
            'phone': extract_phone(resume_text),
            'experience_years': experience,
            'experience_label': get_experience_label(experience),
            'matched_skills': matched_skills,
            'missing_skills': missing_skills,
            'all_skills': all_resume_skills,
            'scores': {
                'tfidf_score': round(tfidf_score, 2),
                'skills_score': round(skills_score, 2),
                'keyword_score': round(keyword_score, 2),
                'final_score': round(final_score, 2)
            }
        }
        
        ranked_results.append(candidate)
    
    # Sort by final score
    ranked_results.sort(key=lambda x: x['scores']['final_score'], reverse=True)
    
    # Add rank and grade
    for i, candidate in enumerate(ranked_results):
        candidate['rank'] = i + 1
        
        score = candidate['scores']['final_score']
        if score >= 65:
            candidate['grade'] = 'Excellent ✅'
        elif score >= 45:
            candidate['grade'] = 'Good 👍'
        elif score >= 25:
            candidate['grade'] = 'Average ⚠️'
        else:
            candidate['grade'] = 'Poor ❌'
    
    return ranked_results