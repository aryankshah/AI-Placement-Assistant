import streamlit as st
import sqlite3
import pandas as pd
from database import save_profile, get_profiles

def profile_page():

    st.header("👤 Student Profile")

    name = st.text_input("Enter Name")
    branch = st.text_input("Enter Branch")

    cgpa = st.number_input(
        "Enter CGPA",
        min_value=0.0,
        max_value=10.0
    )

    skills = st.text_area(
        "Enter Skills (comma separated)"
    )

    if st.button("Save Profile"):

        save_profile(name, branch, cgpa, skills)

        st.success("Profile saved successfully!")

    df = get_profiles()

    st.subheader("Saved Profiles")

    st.dataframe(df)