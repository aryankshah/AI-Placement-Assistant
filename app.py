import pandas as pd
import sqlite3 
import streamlit as st
import pdfplumber
import matplotlib.pyplot as plt
from profile import profile_page
from placement_tracker import placement_tracker_page
from resume_analyser import resume_analyzer_page
from dashboard import dashboard_page
from database import create_tables

create_tables()

st.title("🎯 AI Placement Assistant")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Profile",
        "Placement Tracker",
        "Resume Analyzer",
        "Dashboard"
    ]
)

#home module
if menu == "Home":

    st.header("Welcome!")

    st.write("AI Placement Assistant helps students prepare for placements.")

#profile module
elif menu == "Profile":
    profile_page()

#placement tracker module
elif menu == "Placement Tracker":
    placement_tracker_page()

# resume analyzer module
elif menu == "Resume Analyzer":
    resume_analyzer_page()
    
# dashboard module
elif menu == "Dashboard":
    dashboard_page()