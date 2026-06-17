from resume_parser import extract_text_from_pdf
from preprocessor import extract_skills_from_text, normalize_text
import os

# Find PDF
pdf_files = [f for f in os.listdir('uploads') if f.endswith('.pdf')]

if not pdf_files:
    print("❌ No PDF found! Upload resume first via UI")
    exit()

pdf_path = os.path.join('uploads', pdf_files[0])
print(f"📄 File: {pdf_path}\n")

# Extract text
text = extract_text_from_pdf(pdf_path)

print("=" * 70)
print("📝 RAW EXTRACTED TEXT:")
print("=" * 70)
print(text)
print("\n")

print("=" * 70)
print("🔍 SEARCHING FOR KEY WORDS IN RAW TEXT:")
print("=" * 70)

keywords_to_check = [
    'nlp', 'NLP', 'BERT', 'bert', 'CNN', 'cnn', 'LSTM', 'lstm',
    'neural', 'Neural', 'RAG', 'rag', 'LLM', 'llm', 'Llama', 'llama',
    'computer vision', 'Computer Vision', 'generative', 'Generative',
    'deep learning', 'Deep Learning', 'machine learning', 'Machine Learning',
    'problem', 'Problem', 'agentic', 'Agentic', 'tensorflow', 'TensorFlow',
    'sentiment', 'Sentiment', 'embedding', 'Embedding'
]

for kw in keywords_to_check:
    if kw in text:
        print(f"  ✅ Found: '{kw}'")
    else:
        print(f"  ❌ NOT Found: '{kw}'")

print("\n")
print("=" * 70)
print("🔧 NORMALIZED TEXT (lowercase, no special chars):")
print("=" * 70)
normalized = normalize_text(text)
print(normalized)

print("\n")
print("=" * 70)
print("🎯 SKILLS DETECTED:")
print("=" * 70)
skills = extract_skills_from_text(text)
for s in sorted(skills):
    print(f"  ✅ {s}")
print(f"\n📊 Total: {len(skills)} skills")