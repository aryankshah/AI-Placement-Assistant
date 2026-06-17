import streamlit as st
from database import add_application, get_companies, update_application, delete_application

def placement_tracker_page():

    st.header("🏢 Placement Tracker")

    company_name = st.text_input("Company Name")

    role = st.text_input("Role")

    status = st.selectbox(
        "Application Status",
        [
            "Applied",
            "Interview",
            "Selected",
            "Rejected"
        ]
    )

    if st.button("Add Application"):

        if company_name and role:

            add_application(company_name, role, status)

            st.success("Application added successfully!")

        else:

            st.error("Please fill all fields")

    df = get_companies()

    st.subheader("Applications")

    st.dataframe(df)

    st.subheader("📊 Statistics")

    total = len(df)

    interview_count = len(
        df[df["status"] == "Interview"]
    )

    selected_count = len(
        df[df["status"] == "Selected"]
    )

    rejected_count = len(
        df[df["status"] == "Rejected"]
    )

    applied_count = len(
        df[df["status"] == "Applied"]
    )

    st.write("Applied :", applied_count)

    st.write("Total Applications :", total)

    st.write("Interviews :", interview_count)

    st.write("Selected :", selected_count)

    st.write("Rejected :", rejected_count)

    st.subheader("✏️ Update Application Status")

    application_id = st.number_input(
        "Enter Application ID to Update",
        min_value=1,
        step=1
    )

    new_status = st.selectbox(
        "New Status",
        [
            "Applied",
            "Interview",
            "Selected",
            "Rejected"
        ]
    )

    if st.button("Update Status"):

        update_application(application_id, new_status)

        st.success("Status updated successfully!")

    st.subheader("🗑 Delete Application")

    delete_id = st.number_input(
        "Enter Application ID to Delete",
        min_value=1,
        step=1,
        key="delete"
    )

    if st.button("Delete Application"):

        delete_application(delete_id)

        st.success("Application deleted successfully!")