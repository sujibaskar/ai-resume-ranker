import pandas as pd
from datetime import datetime
import os


def generate_excel_report(ranked_candidates, job_title="Job Position"):
    """Generate Excel HR Report"""
    
    report_data = []
    
    for candidate in ranked_candidates:
        report_data.append({
            'Rank': candidate['rank'],
            'Candidate Name': candidate['name'],
            'Email': candidate['email'],
            'Phone': candidate['phone'],
            'Experience': candidate.get('experience_label', f"{candidate['experience_years']} years"),
            'Final Score (%)': candidate['scores']['final_score'],
            'TF-IDF Score': candidate['scores']['tfidf_score'],
            'Skills Score': candidate['scores']['skills_score'],
            'Keyword Score': candidate['scores']['keyword_score'],
            'Grade': candidate['grade'],
            'Matched Skills': ', '.join(candidate['matched_skills']),
            'Missing Skills': ', '.join(candidate['missing_skills']),
        })
    
    df = pd.DataFrame(report_data)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"HR_Report_{timestamp}.xlsx"
    filepath = os.path.join('uploads', filename)
    
    with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Ranking Report', index=False)
        
        worksheet = writer.sheets['Ranking Report']
        for column in worksheet.columns:
            max_length = max(len(str(cell.value)) for cell in column if cell.value)
            worksheet.column_dimensions[column[0].column_letter].width = min(max_length + 5, 50)
    
    return filename, filepath