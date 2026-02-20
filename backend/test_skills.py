from resume_parser import extract_resume_text
from skill_extractor import extract_skills

text = extract_resume_text("sample_resume.pdf")
skills = extract_skills(text)

print("\n===== DETECTED SKILLS =====\n")
print(skills)