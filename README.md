#  AI-Powered Resume Ranker

An intelligent resume ranking system that uses NLP and Machine Learning to rank candidates based on job descriptions.
## DEMO


<img width="959" height="482" alt="Screenshot 2026-06-17 130338" src="https://github.com/user-attachments/assets/dff5f413-23ec-4925-9d13-48423189a4a3" />
<img width="943" height="483" alt="Screenshot 2026-06-17 130347" src="https://github.com/user-attachments/assets/b2c5f042-acb5-4a8f-b086-989336ce45c9" />
<img width="959" height="458" alt="Screenshot 2026-06-17 130401" src="https://github.com/user-attachments/assets/5734c152-2a4a-4f4b-a999-51f1cbee1964" />
<img width="948" height="449" alt="Screenshot 2026-06-17 130411" src="https://github.com/user-attachments/assets/d6b636c2-bffa-4c47-8e86-7830a243424d" />
<img width="951" height="477" alt="Screenshot 2026-06-17 130427" src="https://github.com/user-attachments/assets/d63f2dd0-ae9d-4f92-bf65-cb0263600f54" />
<img width="956" height="481" alt="Screenshot 2026-06-17 130438" src="https://github.com/user-attachments/assets/2dd91c2d-7026-481e-84e2-5dc4194ab4d3" />
<img width="705" height="332" alt="Screenshot 2026-06-17 130500" src="https://github.com/user-attachments/assets/61ce4d3a-a7e6-420f-b6eb-3c0f8be12d87" />
<img width="709" height="333" alt="Screenshot 2026-06-17 130515" src="https://github.com/user-attachments/assets/702fedea-a7b4-438d-b8c3-7e5e36aada02" />

<img width="716" height="337" alt="Screenshot 2026-06-17 130542" src="https://github.com/user-attachments/assets/cb74b94e-5a9a-45f8-81c3-b3f9c9fdf672" />








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

