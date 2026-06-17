import streamlit as st
import pdfplumber
from gemini_helper import (
    generate_interview_questions,
    generate_skill_gap_analysis,
    generate_resume_suggestions,
    generate_ats_feedback
)

def resume_analyzer_page():     

    st.header("📄 Resume Analyzer")

    detected_skills = []
    missing_skills = []
    text = ""

    target_role = st.selectbox(
        "Select Target Role",
        [
            "Data Analyst",
            "Data Scientist",
            "Software Engineer",
            "Web Developer",
            "AI Engineer"
        ]
    )

    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
        [
            "Resume",
            "ATS Score",
            "Interview Questions",
            "Roadmap",
            "Skill Gap Analysis",
            "Resume Suggestions",
            "ATS Feedback"
        ]
    )

    # ---------------- TAB 1 ----------------
    with tab1:

        uploaded_file = st.file_uploader(
            "Upload Resume",
            type=["pdf"]
        )

        if uploaded_file is not None:

            st.success("Resume uploaded successfully!")

            with pdfplumber.open(uploaded_file) as pdf:

                for page in pdf.pages:

                    page_text = page.extract_text()

                    if page_text:

                        text += page_text

            st.subheader("Extracted Text")

            st.text(text)

            skills_list = [
                "Python",
                "SQL",
                "Pandas",
                "NumPy",
                "Machine Learning",
                "Power BI",
                "Excel",
                "Java",
                "C++",
                "HTML",
                "CSS",
                "JavaScript",
                "Data Science"
            ]

            for skill in skills_list:

                if skill.lower() in text.lower():

                    detected_skills.append(skill)

            st.subheader("Detected Skills")

            st.write(detected_skills)

    # ---------------- TAB 2 ----------------
    with tab2:

        if target_role == "Data Analyst":

            required_skills = [
                "Python",
                "SQL",
                "Excel",
                "Power BI",
                "Pandas"
            ]

        elif target_role == "Data Scientist":

            required_skills = [
                "Python",
                "SQL",
                "Pandas",
                "NumPy",
                "Machine Learning",
                "Statistics"
            ]

        elif target_role == "Software Engineer":

            required_skills = [
                "Python",
                "Java",
                "SQL",
                "Git",
                "DSA"
            ]

        elif target_role == "Web Developer":

            required_skills = [
                "HTML",
                "CSS",
                "JavaScript",
                "React",
                "SQL"
            ]

        else:

            required_skills = [
                "Python",
                "Machine Learning",
                "Deep Learning",
                "NumPy",
                "Pandas"
            ]

        matched_skills = 0
        missing_skills = []

        for skill in required_skills:

            if skill in detected_skills:

                matched_skills += 1

            else:

                missing_skills.append(skill)

        ats_score = (matched_skills / len(required_skills)) * 100

        st.subheader("🎯 ATS Score")

        st.progress(int(ats_score))

        st.write(round(ats_score, 2), "%")

        st.subheader("❌ Missing Skills")

        for skill in missing_skills:

            st.write("•", skill)

    # ---------------- TAB 3 ----------------
    with tab3:

        st.subheader("🤖 AI Interview Questions")

        if st.button("Generate Questions"):

            try:

                with st.spinner("Generating AI Interview Questions..."):

                    response = generate_interview_questions(
                    target_role,
                    detected_skills
                    )

                st.success("AI Interview Questions generated successfully!")

                with st.expander("View AI Interview Questions"):
                    st.write(response)

            except Exception as e:

                st.error(f"Gemini Error: {e}")

    # ---------------- TAB 4 ----------------
    with tab4:

        roadmap_dict = {

            "Excel": [
                "Learn formulas",
                "Pivot tables",
                "Data cleaning"
            ],

            "Power BI": [
                "Power Query",
                "DAX",
                "Dashboard creation"
            ],

            "DSA": [
                "Arrays",
                "Strings",
                "Linked Lists",
                "Trees",
                "LeetCode practice"
            ],

            "Git": [
                "Git commands",
                "GitHub",
                "Version control"
            ],

            "Machine Learning": [
                "Regression",
                "Classification",
                "Scikit-learn"
            ],

            "Deep Learning": [
                "Neural Networks",
                "TensorFlow",
                "CNN"
            ],

            "Statistics": [
                "Mean and median",
                "Probability",
                "Hypothesis testing"
            ],

            "React": [
                "Components",
                "Props and State",
                "Hooks"
            ]
        }

        st.subheader("Learning Roadmap")

        for skill in missing_skills:

            st.subheader(skill)

            if skill in roadmap_dict:

                for topic in roadmap_dict[skill]:

                    st.write("•", topic)

            else:

                st.write("• Learn basics")

    # ---------------- TAB 5 ----------------
    with tab5:

        st.subheader("🧠 AI Skill Gap Analysis")

        if st.button("Analyze Skill Gap"):

            try:
                
                with st.spinner("Analyzing Skill Gap..."):
                    analysis = generate_skill_gap_analysis(
                    target_role,
                    detected_skills
                )
                st.success("AI Skill Gap Analysis generated successfully!")

                with st.expander("View AI Skill Gap Analysis"):
                    st.write(analysis)

            except Exception as e:

                st.error(f"Gemini Error: {e}")

    # ---------------- TAB 6 ----------------
    with tab6:

        st.subheader("📝 AI Resume Suggestions")

        if st.button("Generate Resume Suggestions"):

            if text:

                try:

                    with st.spinner("Generating AI Resume Suggestions..."):
                        suggestions = generate_resume_suggestions(text)

                    st.success("AI Resume Suggestions generated successfully!")

                    with st.expander("View AI Resume Suggestions"):
                        st.write(suggestions)

                except Exception as e:

                    st.error(f"Gemini Error: {e}")

            else:

                st.warning("Please upload a resume first.")

    # ---------------- TAB 7 ----------------
    with tab7:

        st.subheader("📄 AI ATS Feedback")

        if st.button("Generate ATS Feedback"):

            if text:

                try:
                    
                    with st.spinner("Generating AI ATS Feedback..."):
                        feedback = generate_ats_feedback(
                        target_role,
                        detected_skills,
                        text
                    )

                    st.success("AI ATS Feedback generated successfully!")
                    
                    with st.expander("View AI ATS Feedback"):
                        st.write(feedback)

                except Exception as e:

                    st.error(f"Gemini Error: {e}")

            else:

                st.warning("Please upload a resume first.")