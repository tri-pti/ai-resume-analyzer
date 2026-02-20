from resume_parser import extract_resume_text
from skill_extractor import extract_skills
from ats_score import calculate_ats_score
from job_matcher import get_job_skills

text = extract_resume_text("sample_resume.pdf")
resume_skills = extract_skills(text)

job_role = "AI Engineer"
required_skills = get_job_skills(job_role)

score, matched, missing = calculate_ats_score(resume_skills, required_skills)

print("\n====== ATS REPORT ======\n")
print("Job Role:", job_role)
print("ATS Score:", score, "%")
print("Matched Skills:", matched)
print("Missing Skills:", missing)