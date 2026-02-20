from ats_score import calculate_ats_score

JOB_ROLES = {
    "AI Engineer": [
        "python","machine learning","deep learning","nlp","tensorflow","pytorch"
    ],
    "Web Developer": [
        "html","css","javascript","react","node","flask"
    ],
    "Data Analyst": [
        "python","sql","power bi","pandas","excel"
    ]
}


def get_job_skills(role):
    return JOB_ROLES.get(role, [])


def predict_best_role(resume_skills):
    best_role = None
    best_score = 0

    for role, skills in JOB_ROLES.items():
        score, _, _ = calculate_ats_score(resume_skills, skills)

        if score > best_score:
            best_score = score
            best_role = role

    return best_role, round(best_score, 2)

def compare_all_roles(resume_skills):
    role_scores = {}

    for role, skills in JOB_ROLES.items():
        score, _, _ = calculate_ats_score(resume_skills, skills)
        role_scores[role] = round(score, 2)

    return role_scores