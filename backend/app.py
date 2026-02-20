from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from suggestions import generate_suggestions
from resume_parser import extract_resume_text
from skill_extractor import extract_skills
from ats_score import calculate_ats_score
from job_matcher import get_job_skills
from job_matcher import compare_all_roles

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return "Resume Analyzer API Running"


@app.route("/analyze-resume", methods=["POST"])
def analyze_resume():
    if "resume" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["resume"]
    job_role = request.form.get("job_role", "AI Engineer")

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # process resume
    text = extract_resume_text(filepath)
    skills = extract_skills(text)

    required_skills = get_job_skills(job_role)
    score, matched, missing = calculate_ats_score(skills, required_skills)

    from job_matcher import predict_best_role
    best_role, role_score = predict_best_role(skills)
    all_role_scores = compare_all_roles(skills)
    suggestions = generate_suggestions(job_role, missing, skills)

    return jsonify({
    "job_role": job_role,
    "ats_score": score,
    "detected_skills": skills,
    "matched_skills": matched,
    "missing_skills": missing,
    "recommended_role": best_role,
    "role_match_score": role_score,
    "role_comparison": all_role_scores,
    "suggestions": suggestions
})


if __name__ == "__main__":
    app.run(debug=True)