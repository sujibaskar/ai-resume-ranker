from preprocessor import extract_skills_from_text, normalize_text
from resume_parser import extract_text_from_pdf
import os

# Test with your actual resume
pdf_files = [f for f in os.listdir('uploads') if f.endswith('.pdf')]

if pdf_files:
    pdf_path = os.path.join('uploads', pdf_files[0])
    print(f"📄 Testing: {pdf_path}\n")
    
    # Extract text
    text = extract_text_from_pdf(pdf_path)
    
    print("=" * 60)
    print("📝 EXTRACTED TEXT (first 1000 chars):")
    print("=" * 60)
    print(text[:1000])
    
    print("\n" + "=" * 60)
    print("🔧 NORMALIZED TEXT (first 1000 chars):")
    print("=" * 60)
    print(normalize_text(text)[:1000])
    
    print("\n" + "=" * 60)
    print("🎯 DETECTED SKILLS:")
    print("=" * 60)
    skills = extract_skills_from_text(text)
    for skill in sorted(skills):
        print(f"  ✅ {skill}")
    
    print(f"\n📊 Total Skills Detected: {len(skills)}")
else:
    print("❌ No PDF found in uploads folder")