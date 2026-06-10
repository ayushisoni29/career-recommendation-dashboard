import streamlit as st
import requests

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="AI Career System", layout="wide")

# ---------- CUSTOM CSS (MODERN UI) ----------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.main-title {
    font-size: 40px;
    font-weight: bold;
    color: #00C9A7;
}
.card {
    padding: 20px;
    border-radius: 15px;
    background: #1c1f26;
    color: white;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown('<p class="main-title">🚀 AI Career Intelligence System</p>', unsafe_allow_html=True)
st.write("Get smart career recommendations with real-world insights")

# ---------- LAYOUT ----------
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📊 Academic Profile")
    marks = st.slider("Marks", 0, 100, 80)
    interest = st.selectbox("Interest", ["tech", "business", "design"])
    skills = st.text_input("Skills (e.g. python, marketing)")

with col2:
    st.markdown("### 🧠 Aptitude Analysis")
    logical = st.slider("Logical Thinking", 1, 10, 5)
    creativity = st.slider("Creativity", 1, 10, 5)
    communication = st.slider("Communication", 1, 10, 5)

# ---------- BUTTON ----------
if st.button("🔥 Get Recommendation"):

    try:
        response = requests.post(
            "http://127.0.0.1:5000/predict",
            json={
                "marks": marks,
                "interest": interest,
                "skills": skills,
                "logical": logical,
                "creativity": creativity,
                "communication": communication
            },
            timeout=5
        )

        # 🔥 Check if response is OK
        if response.status_code == 200:

            data = response.json()

            st.success("✅ Recommendation Generated Successfully!")

            # ---------- RESULT UI ----------
            st.markdown("## 🎯 Career Recommendation")
            st.markdown(f'<div class="card"><h2>{data.get("career", "N/A")}</h2></div>', unsafe_allow_html=True)

            st.markdown("## 📊 Market Insights")
            st.markdown(f'''
            <div class="card">
                <p>🚀 <b>Demand:</b> {data.get("demand", "N/A")}</p>
                <p>💰 <b>Salary:</b> {data.get("salary", "N/A")}</p>
                <p>🏢 <b>Companies:</b> {data.get("companies", "N/A")}</p>
            </div>
            ''', unsafe_allow_html=True)

            st.markdown("## 🧠 Skills Required")
            st.markdown(f'<div class="card">{data.get("skills", "N/A")}</div>', unsafe_allow_html=True)

            st.markdown("## 🛣 Career Roadmap")
            st.markdown(f'<div class="card">{data.get("roadmap", "N/A")}</div>', unsafe_allow_html=True)

        else:
            st.error(f"❌ Server Error: {response.status_code}")

    except requests.exceptions.ConnectionError:
        st.error("❌ Backend not running! Please start Flask server.")

    except requests.exceptions.Timeout:
        st.error("⏳ Server timeout! Try again.")

    except Exception as e:
        st.error(f"⚠️ Error: {e}")