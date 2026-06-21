import streamlit as st
import matplotlib.pyplot as plt
from database import get_application_statistics


def dashboard_page():

    st.header("📊 Dashboard")

    (
        total,
        applied_count,
        interview_count,
        selected_count,
        rejected_count
    ) = get_application_statistics()

    # Statistics
    st.subheader("Placement Statistics")

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Total", total)
    col2.metric("Applied", applied_count)
    col3.metric("Interview", interview_count)
    col4.metric("Selected", selected_count)
    col5.metric("Rejected", rejected_count)

    # Bar Chart
    st.subheader("📈 Application Status Chart")

    labels = [
        "Applied",
        "Interview",
        "Selected",
        "Rejected"
    ]

    values = [
        applied_count,
        interview_count,
        selected_count,
        rejected_count
    ]

    fig, ax = plt.subplots()

    ax.bar(
        labels,
        values,
        color=["blue", "orange", "green", "red"]
    )

    ax.set_xlabel("Status")

    ax.set_ylabel("Count")

    ax.set_title("Application Status")

    st.pyplot(fig)

    # Pie Chart
    st.subheader("🥧 Application Distribution")

    fig2, ax2 = plt.subplots()

    if sum(values) > 0:

        ax2.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        colors=["blue", "orange", "green", "red"]
        )

        ax2.set_title("Applications Distribution")

        st.pyplot(fig2)

    else:

        st.info("No applications available to display the pie chart.")

    # Success Rate
    st.subheader("🎯 Placement Success Rate")

    if total > 0:
        success_rate = (selected_count / total) * 100
    else:
        success_rate = 0

    st.progress(int(success_rate))

    st.write("Success Rate :", round(success_rate, 2), "%")

    # Interview Rate
    st.subheader("🎤 Interview Rate")

    if total > 0:
        interview_rate = (interview_count / total) * 100
    else:
        interview_rate = 0

    st.progress(int(interview_rate))

    st.write("Interview Rate :", round(interview_rate, 2), "%")