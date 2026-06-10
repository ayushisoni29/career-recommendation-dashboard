import pandas as pd

# agar dataset use karna hai to rakho warna optional hai
# data = pd.read_excel("career_dataset.xlsx")

def predict_career(marks, interest, skills, logical, creativity, communication):
    score = logical + creativity + communication
    skills_list = [s.strip().lower() for s in skills.split(',') if s.strip()]
    teaching_terms = ["teaching", "research", "education", "academia", "mentoring", "lecture", "presentation"]
    has_teaching_experience = any(
        any(term in skill for term in teaching_terms) for skill in skills_list
    )

    if interest == "education" or has_teaching_experience:
        if marks >= 70 or score >= 18:
            return "Assistant Professor"
        return "Academic Researcher"

    if interest == "tech":
        if score >= 22:
            return "Data Scientist"
        return "Software Engineer"

    if interest == "business":
        return "Business Analyst"

    if interest == "design":
        return "UI/UX Designer"

    return "General Career Advisor"
