#  AI-Powered Resume Ranker

An intelligent resume ranking system that uses NLP and Machine Learning to rank candidates based on job descriptions.

##  Features

-  PDF Resume Parsing
-  SpaCy NLP Preprocessing
-  TF-IDF Vectorization
-  Smart Skills Matching (150+ skills)
-  Implied Skills Detection (BERT → NLP)
-  Multi-factor Scoring Algorithm
-  Experience Auto-detection
-  HR Report Excel Download
-  Beautiful React UI

##  Tech Stack

### Backend
- Python 3.x
- Flask
- SpaCy
- Scikit-learn
- pdfplumber
- pandas

### Frontend
- React.js
- Axios
- CSS3

##  Installation

### Backend Setup
\```bash
cd backend
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python app.py
\```

### Frontend Setup
\```bash
cd frontend
npm install
npm start
\```

##  Usage

1. Open browser: `http://localhost:3000`
2. Enter job title and description
3. Upload PDF resumes (multiple allowed)
4. Click "Rank Resumes"
5. View ranked results
6. Download HR Excel report

##  Scoring Algorithm

\```
Final Score = (TF-IDF × 15%) + (Skills × 70%) + (Keywords × 15%)

Grades:
- 65%+ → Excellent 
- 45%+ → Good 
- 25%+ → Average 
- Below → Poor 
\```

##  Project Structure

\```
ResumeRanker/
├── backend/
│   ├── app.py
│   ├── resume_parser.py
│   ├── preprocessor.py
│   ├── ranker.py
│   ├── report_generator.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── App.js
│   │   └── App.css
│   └── package.json
└── README.md
\```

##  Author

**Sujitha B**
- GitHub: [@sujibaskar](https://github.com/sujibaskar)
- Email: bsujitha186@gmail.com

