from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
from resume_parser import process_multiple_resumes
from ranker import rank_resumes
from report_generator import generate_excel_report

app = Flask(__name__)
CORS(app)  # Allow React frontend to connect

# Upload folder
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max


@app.route('/')
def home():
    return jsonify({
        'message': '🚀 Resume Ranker API Running',
        'version': '1.0'
    })


@app.route('/api/rank', methods=['POST'])
def rank_resumes_api():
    """
    Main API endpoint
    - Accept multiple PDF resumes
    - Accept job description
    - Return ranked results
    """
    
    try:
        # Get job description
        job_description = request.form.get('job_description', '')
        job_title = request.form.get('job_title', 'Job Position')
        
        if not job_description:
            return jsonify({'error': 'Job description is required'}), 400
        
        # Get uploaded files
        files = request.files.getlist('resumes')
        
        if not files or len(files) == 0:
            return jsonify({'error': 'At least one resume is required'}), 400
        
        # Clear old uploads
        for old_file in os.listdir(UPLOAD_FOLDER):
            if old_file.endswith('.pdf'):
                os.remove(os.path.join(UPLOAD_FOLDER, old_file))
        
        # Save uploaded PDFs
        saved_files = []
        for file in files:
            if file.filename.endswith('.pdf'):
                filepath = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(filepath)
                saved_files.append(file.filename)
        
        if not saved_files:
            return jsonify({'error': 'No valid PDF files uploaded'}), 400
        
        # Extract text from all resumes
        resumes = process_multiple_resumes(UPLOAD_FOLDER)
        
        if not resumes:
            return jsonify({'error': 'Could not extract text from resumes'}), 400
        
        # Rank resumes
        ranked_results = rank_resumes(job_description, resumes)
        
        # Generate Excel report
        report_filename, _ = generate_excel_report(ranked_results, job_title)
        
        return jsonify({
            'success': True,
            'total_candidates': len(ranked_results),
            'job_title': job_title,
            'ranked_candidates': ranked_results,
            'report_filename': report_filename
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/download/<filename>', methods=['GET'])
def download_report(filename):
    """Download HR report"""
    try:
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        return send_file(
            filepath,
            as_attachment=True,
            download_name=filename
        )
    except Exception as e:
        return jsonify({'error': 'File not found'}), 404


@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'message': 'API is running'})


if __name__ == '__main__':
    app.run(debug=True, port=5000)