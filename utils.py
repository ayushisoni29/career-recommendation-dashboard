import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SKILLS_PATH = os.path.join(BASE_DIR, "skills_dataset.xlsx")
ROADMAP_PATH = os.path.join(BASE_DIR, "roadmap_dataset.xlsx")


def load_data(path):
    if os.path.exists(path):
        try:
            return pd.read_excel(path)
        except Exception:
            return pd.DataFrame()
    return pd.DataFrame()


skills_data = load_data(SKILLS_PATH)
roadmap_data = load_data(ROADMAP_PATH)

CAREER_REQUIRED_SKILLS = {
    "Data Scientist": ["python", "statistics", "machine learning", "data analysis", "sql"],
    "Software Engineer": ["python", "java", "problem solving", "data structures", "algorithms"],
    "Business Analyst": ["excel", "communication", "business analysis", "data visualization", "stakeholder management"],
    "UI/UX Designer": ["design", "sketch", "figma", "user research", "prototyping"],
    "Assistant Professor": ["teaching", "research", "curriculum development", "public speaking", "academic writing"],
    "Academic Researcher": ["research", "data analysis", "experimental design", "report writing", "scholarship"],
}

CAREER_INSIGHTS = {
    "Data Scientist": "This path fits students who enjoy solving problems with data, pattern finding, and turning numbers into decisions.",
    "Software Engineer": "The role matches learners who like building applications, coding logically, and creating reliable systems.",
    "Business Analyst": "Choose this when you enjoy bridging technical and business ideas, analyzing trends, and communicating insights clearly.",
    "UI/UX Designer": "This role is ideal for creative minds who care deeply about user experience, design thinking, and product storytelling.",
    "Assistant Professor": "This recommendation is for people who want to teach, mentor, and guide students while continuing academic research.",
    "Academic Researcher": "This role suits those who want to explore research questions deeply and contribute new knowledge in their field.",
}

FUTURE_TRENDS = {
    "Data Scientist": "Data-driven education and AI projects are expanding fast.",
    "Software Engineer": "Software skills remain in demand across startups and education platforms.",
    "Business Analyst": "Decision-focused roles are growing with analytics in every sector.",
    "UI/UX Designer": "Design and usability skills are increasingly critical for digital learning products.",
    "Assistant Professor": "Education and higher learning roles remain essential as institutions seek experienced mentors.",
    "Academic Researcher": "Research careers are growing with funding for innovation, publications, and cross-disciplinary work.",
}

MARKET_DATA = {
    "Data Scientist": {
        "demand": "High 🔥",
        "salary": "₹6L - ₹20L",
        "companies": "Google, Amazon, Microsoft",
        "future_trends": FUTURE_TRENDS["Data Scientist"],
    },
    "Software Engineer": {
        "demand": "Very High 🚀",
        "salary": "₹4L - ₹15L",
        "companies": "Infosys, TCS, Wipro",
        "future_trends": FUTURE_TRENDS["Software Engineer"],
    },
    "Business Analyst": {
        "demand": "Medium",
        "salary": "₹5L - ₹12L",
        "companies": "Deloitte, EY",
        "future_trends": FUTURE_TRENDS["Business Analyst"],
    },
    "UI/UX Designer": {
        "demand": "Growing 📈",
        "salary": "₹4L - ₹10L",
        "companies": "Adobe, Zomato",
        "future_trends": FUTURE_TRENDS["UI/UX Designer"],
    },
    "Assistant Professor": {
        "demand": "Stable and respected",
        "salary": "₹5L - ₹12L",
        "companies": "Universities, Colleges, Research Institutes",
        "future_trends": FUTURE_TRENDS["Assistant Professor"],
    },
    "Academic Researcher": {
        "demand": "Growing",
        "salary": "₹4L - ₹10L",
        "companies": "Research Labs, Universities, Think Tanks",
        "future_trends": FUTURE_TRENDS["Academic Researcher"],
    },
}


def get_skills(career):
    row = skills_data[skills_data["career"] == career]
    if not row.empty:
        return row.iloc[0]["required_skills"]
    return "No skills found"

def get_roadmap(career):
    row = roadmap_data[roadmap_data["career"] == career]
    if not row.empty:
        return row.iloc[0]["roadmap_steps"]
    return "No roadmap found"


def calculate_career_fit(marks, interest, logical, creativity, communication, skills_list, career):
    aptitude = logical + creativity + communication
    interest_score = {"tech": 10, "business": 8, "design": 9, "education": 9}.get(interest, 7)
    skill_match = 0
    required = CAREER_REQUIRED_SKILLS.get(career, [])

    for skill in required:
        if any(skill in entry for entry in skills_list):
            skill_match += 1

    bonus = min(20, skill_match * 4)
    fit = int(min(100, marks * 0.35 + aptitude * 4 + interest_score * 2 + bonus))
    return fit


def analyze_skill_gap(career, skills_list):
    required = CAREER_REQUIRED_SKILLS.get(career, [])
    missing = [skill for skill in required if not any(skill in entry for entry in skills_list)]

    if not missing:
        return "Great! Your skills align well with this career path. Keep enhancing them with projects."

    return f"Focus on these next: {', '.join(missing[:4])}. These skills improve your education-to-career readiness."


def get_personalized_strength(logical, creativity, communication):
    scores = {
        "Logical Thinking": logical,
        "Creativity": creativity,
        "Communication": communication,
    }
    sorted_strengths = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    top_strengths = [f"{name} ({value}/10)" for name, value in sorted_strengths]
    return ", ".join(top_strengths)


def get_role_insight(career):
    return CAREER_INSIGHTS.get(career, "This recommendation is built to support your education goals with a clear next step.")


def get_market_data(career):
    return MARKET_DATA.get(career, {})