import pdfplumber
import os

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF file"""
    text = ""
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"Error extracting {pdf_path}: {e}")
        return ""
    
    return text.strip()


def extract_candidate_name(pdf_path):
    """Extract filename as candidate name"""
    filename = os.path.basename(pdf_path)
    name = filename.replace('.pdf', '').replace('_', ' ').replace('-', ' ')
    return name.title()


def process_multiple_resumes(upload_folder):
    """Process all PDFs in upload folder"""
    resumes = []
    
    for filename in os.listdir(upload_folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(upload_folder, filename)
            text = extract_text_from_pdf(pdf_path)
            name = extract_candidate_name(pdf_path)
            
            if text:
                resumes.append({
                    'filename': filename,
                    'name': name,
                    'text': text
                })
    
    return resumes