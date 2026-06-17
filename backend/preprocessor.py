import spacy
import re

nlp = spacy.load('en_core_web_sm')

# 🚀 EXPANDED SKILLS DATABASE
SKILLS_DATABASE = [
    # Programming Languages
    'python', 'java', 'javascript', 'typescript', 'c++', 'c#', 'ruby', 
    'golang', 'php', 'swift', 'kotlin', 'scala',
    
    # Web Development
    'react', 'reactjs', 'angular', 'vue', 'nodejs', 'node.js', 'express',
    'html', 'css', 'bootstrap', 'tailwind', 'jquery', 'next.js',
    'fullstack', 'full stack', 'frontend', 'backend',
    
    # Databases
    'mongodb', 'sql', 'mysql', 'postgresql', 'redis', 'firebase',
    'oracle', 'sqlite',
    
    # ML/AI Core
    'machine learning', 'deep learning', 'neural network', 'neural networks',
    'artificial intelligence', 'data science', 'data analytics',
    'predictive modeling',
    
    # NLP
    'nlp', 'natural language processing', 'bert', 'transformer', 'transformers',
    'textblob', 'sentiment analysis', 'text mining', 'word embedding',
    'embeddings', 'tokenization',
    
    # Computer Vision
    'computer vision', 'opencv', 'image processing', 'object detection',
    'cnn', 'convolutional neural network', 'image classification',
    
    # Deep Learning Models
    'lstm', 'rnn', 'gru', 'gan', 'bilstm', 'autoencoder',
    
    # Generative AI / LLMs
    'generative ai', 'genai', 'llm', 'llms', 'large language model',
    'langchain', 'llama', 'gpt', 'chatgpt', 'openai', 'huggingface',
    'rag', 'retrieval augmented generation', 'prompt engineering',
    'chroma', 'pinecone', 'faiss', 'vector database', 'agentic ai',
    'agents', 'agentic',
    
    # ML Frameworks
    'tensorflow', 'pytorch', 'keras', 'scikit-learn', 'sklearn',
    'pandas', 'numpy', 'matplotlib', 'seaborn', 'spacy', 'nltk',
    'xgboost', 'lightgbm',
    
    # Big Data
    'spark', 'apache spark', 'pyspark', 'hadoop', 'kafka',
    'big data', 'data pipeline', 'data pipelines', 'etl',
    
    # Cloud & DevOps
    'aws', 'azure', 'gcp', 'google cloud', 'cloud computing',
    'docker', 'kubernetes', 'jenkins', 'ci/cd', 'devops',
    
    # Tools
    'git', 'github', 'gitlab', 'jira', 'postman',
    'vscode', 'jupyter', 'jupyter notebook', 'google colab', 'colab',
    'linux', 'unix', 'bash',
    
    # Backend Frameworks
    'flask', 'django', 'fastapi', 'spring boot', 'rest api', 'restful',
    'graphql', 'microservices', 'api development', 'api',
    
    # Mobile
    'flutter', 'react native', 'android', 'ios',
    
    # Data Concepts
    'data visualization', 'data wrangling', 'feature engineering',
    'model evaluation', 'model deployment', 'mlops', 'model serving',
    'data ingestion', 'data quality', 'preprocessing',
    
    # Soft Skills
    'leadership', 'communication', 'teamwork', 'problem solving',
    'analytical thinking', 'project management', 'agile', 'scrum',
    'collaboration',
    
    # Business
    'business intelligence', 'consulting', 'decision intelligence',
    'enterprise', 'automation', 'deployment',
]

# 🔗 SYNONYMS
SKILL_SYNONYMS = {
    'ml': 'machine learning',
    'dl': 'deep learning',
    'ai': 'artificial intelligence',
    'cv': 'computer vision',
    'gen ai': 'generative ai',
    'genai': 'generative ai',
    'js': 'javascript',
    'k8s': 'kubernetes',
    'tf': 'tensorflow',
    'nn': 'neural network',
}

# 🧠 IMPLIED SKILLS - If you have X, you implicitly know Y
IMPLIED_SKILLS = {
    'nlp': ['bert', 'textblob', 'sentiment analysis', 'embeddings', 'transformer'],
    'natural language processing': ['bert', 'textblob', 'sentiment analysis'],
    'neural network': ['cnn', 'lstm', 'gru', 'bilstm', 'deep learning'],
    'neural networks': ['cnn', 'lstm', 'gru', 'bilstm', 'deep learning'],
    'generative ai': ['rag', 'llm', 'llms', 'llama', 'langchain', 'agentic', 'chroma', 'faiss'],
    'tensorflow': ['cnn', 'lstm', 'deep learning'],
    'computer vision': ['cnn', 'image processing', 'opencv'],
    'problem solving': ['analytical thinking', 'machine learning', 'deep learning'],
    'data wrangling': ['pandas', 'numpy', 'preprocessing'],
    'data pipelines': ['etl', 'fastapi', 'api'],
    'model serving': ['fastapi', 'flask', 'api'],
    'data ingestion': ['api', 'fastapi'],
    'langchain': ['rag', 'llm', 'agentic', 'chroma', 'faiss'],
    'deployment': ['fastapi', 'docker', 'flask'],
    'data quality': ['preprocessing', 'feature engineering'],
    'enterprise': ['fullstack', 'api', 'backend'],
    'automation': ['agentic'],
    'analytical thinking': ['data science', 'machine learning'],
    'decision intelligence': ['data science', 'machine learning'],
    'mlops': ['deployment', 'docker'],
}


def normalize_text(text):
    """Normalize text for better matching"""
    text = re.sub(r'\s+', ' ', text)
    text = text.lower()
    text = text.replace('/', ' ').replace('-', ' ').replace('\\', ' ')
    text = text.replace(',', ' ').replace('.', ' ').replace(':', ' ')
    text = text.replace('(', ' ').replace(')', ' ').replace('|', ' ')
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def clean_text(text):
    text = re.sub(r'[^\w\s\+\#]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.lower().strip()
    return text


def preprocess_with_spacy(text):
    cleaned = clean_text(text)
    doc = nlp(cleaned)
    
    tokens = [
        token.lemma_  
        for token in doc
        if not token.is_stop 
        and not token.is_punct 
        and len(token.text) > 1
    ]
    
    return ' '.join(tokens)


def extract_skills_from_text(text):
    """Extract skills with flexible matching"""
    normalized = normalize_text(text)
    raw_lower = text.lower()
    found_skills = set()
    
    for skill in SKILLS_DATABASE:
        skill_lower = skill.lower()
        skill_normalized = normalize_text(skill)
        
        # Method 1: Check in normalized text
        if ' ' not in skill_normalized:
            pattern = r'\b' + re.escape(skill_normalized) + r'\b'
            if re.search(pattern, normalized):
                found_skills.add(skill)
                continue
        else:
            words = skill_normalized.split()
            pattern = r'\b' + r'\s+'.join(re.escape(w) for w in words) + r'\b'
            if re.search(pattern, normalized):
                found_skills.add(skill)
                continue
        
        # Method 2: Raw text check
        if skill_lower in raw_lower:
            found_skills.add(skill)
    
    # Synonyms
    for alias, canonical in SKILL_SYNONYMS.items():
        pattern = r'\b' + re.escape(alias.lower()) + r'\b'
        if re.search(pattern, normalized) or re.search(pattern, raw_lower):
            found_skills.add(canonical)
    
    return list(found_skills)


def extract_skills_with_implied(text):
    """Extract direct skills + implied parent skills"""
    direct_skills = extract_skills_from_text(text)
    skills_set = set(direct_skills)
    
    for parent_skill, child_skills in IMPLIED_SKILLS.items():
        if any(child in skills_set for child in child_skills):
            skills_set.add(parent_skill)
    
    return list(skills_set)


def extract_email(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, text)
    return emails[0] if emails else "Not Found"


def extract_phone(text):
    """Better phone extraction"""
    patterns = [
        r'\+91[\s-]?[6-9]\d{9}',
        r'\b[6-9]\d{9}\b',
        r'\+\d{1,3}[\s-]?\d{10}',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(0)
    
    return "Not Found"


def extract_experience_years(text):
    """Extract years of experience - improved detection"""
    text_lower = text.lower()
    
    # Method 1: Direct year mentions
    patterns = [
        r'(\d+)\+?\s*years?\s*of\s*experience',
        r'(\d+)\+?\s*years?\s*experience',
        r'experience\s*of\s*(\d+)\+?\s*years?',
        r'(\d+)\+?\s*yrs?\s*experience',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text_lower)
        if match:
            return float(match.group(1))
    
    # Method 2: Calculate from date ranges
    # Pattern: "Dec 2024-Jan 2025" or "Jan 2023 - Dec 2024"
    date_pattern = r'(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s*(\d{4})\s*[-–to]+\s*(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s*(\d{4})'
    
    months_map = {
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
        'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
    }
    
    total_months = 0
    matches = re.findall(date_pattern, text_lower)
    
    for match in matches:
        start_month, start_year, end_month, end_year = match
        start = int(start_year) * 12 + months_map.get(start_month[:3], 1)
        end = int(end_year) * 12 + months_map.get(end_month[:3], 1)
        months = max(0, end - start) + 1
        total_months += months
    
    if total_months > 0:
        years = round(total_months / 12, 1)
        return years
    
    # Method 3: Internship detection
    if 'intern' in text_lower:
        return 0.1
    
    return 0


def get_experience_label(years):
    """Get a friendly label for experience"""
    if years == 0:
        return "Fresher"
    elif years < 0.5:
        return "Internship Experience"
    elif years < 1:
        months = int(years * 12)
        return f"{months} months exp."
    elif years == 1:
        return "1 year exp."
    else:
        return f"{years} years exp."


def extract_name_from_text(text):
    """Extract name from resume content"""
    lines = text.strip().split('\n')
    for line in lines[:5]:
        line = line.strip()
        if line and 2 <= len(line.split()) <= 4:
            words = line.split()
            if all(w.replace('.', '').isalpha() for w in words):
                if line.isupper() or line.istitle():
                    return line.title()
    return None