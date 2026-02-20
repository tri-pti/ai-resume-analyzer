def calculate_ats_score(resume_skills, job_required_skills):
    """
    Calculates ATS score based on matching skills
    """

    resume_skills = set([skill.lower() for skill in resume_skills])
    job_required_skills = set([skill.lower() for skill in job_required_skills])

    matched_skills = resume_skills.intersection(job_required_skills)

    if len(job_required_skills) == 0:
        return 0, [], []

    score = (len(matched_skills) / len(job_required_skills)) * 100

    missing_skills = job_required_skills - resume_skills

    return round(score, 2), list(matched_skills), list(missing_skills)