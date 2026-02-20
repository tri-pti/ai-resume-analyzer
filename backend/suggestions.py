def generate_suggestions(job_role, missing_skills, detected_skills):
    suggestions = []

    # skill based suggestions
    for skill in missing_skills:
        suggestions.append(f"Consider learning or adding projects using {skill}")

    # project suggestions
    if "machine learning" in missing_skills:
        suggestions.append("Add at least one Machine Learning project with dataset and results")

    if "deep learning" in missing_skills:
        suggestions.append("Include a deep learning project (CNN, LSTM, or Transformer)")

    if "sql" not in detected_skills:
        suggestions.append("Add database or SQL project to strengthen backend/data skills")

    # resume quality suggestions
    if len(detected_skills) < 8:
        suggestions.append("Your resume has low technical keyword density — add more tools & technologies")

    suggestions.append("Add GitHub links to your projects for credibility")

    return suggestions