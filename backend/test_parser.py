from resume_parser import extract_resume_text

text = extract_resume_text("sample_resume.pdf")

print("\n========= RESUME TEXT =========\n")
print(text[:1500])  # first part only