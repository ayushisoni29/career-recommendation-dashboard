from flask import Flask, render_template, request
from model import predict_career
from utils import (
    get_skills,
    get_roadmap,
    get_market_data,
    calculate_career_fit,
    analyze_skill_gap,
    get_personalized_strength,
    get_role_insight,
)

app = Flask(__name__)


def parse_int_field(value, min_value=0, max_value=10):
    try:
        number = int(value)
    except (ValueError, TypeError):
        return min_value
    return max(min_value, min(max_value, number))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():

    marks = parse_int_field(request.form.get('marks'), 0, 100)
    interest = request.form['interest']
    skills = request.form['skills']

    logical = parse_int_field(request.form.get('logical'))
    creativity = parse_int_field(request.form.get('creativity'))
    communication = parse_int_field(request.form.get('communication'))

    career = predict_career(marks, interest, skills, logical, creativity, communication)

    skills_data = get_skills(career)
    roadmap = get_roadmap(career)
    market = get_market_data(career)

    skills_list = [s.strip().lower() for s in skills.split(',') if s.strip()]
    fit_score = calculate_career_fit(
        marks,
        interest,
        logical,
        creativity,
        communication,
        skills_list,
        career,
    )
    skill_gap = analyze_skill_gap(career, skills_list)
    strengths = get_personalized_strength(logical, creativity, communication)
    insight = get_role_insight(career)

    return render_template(
        "result.html",
        career=career,
        skills=skills_data,
        roadmap=roadmap,
        demand=market.get("demand"),
        salary=market.get("salary"),
        companies=market.get("companies"),
        fit_score=fit_score,
        skill_gap=skill_gap,
        strengths=strengths,
        insight=insight,
        future_trends=market.get("future_trends"),
    )

if __name__ == '__main__':
    app.run(debug=True)