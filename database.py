import sqlite3
import pandas as pd


# Connection
def get_connection():

    conn = sqlite3.connect("placement.db")

    return conn


# ---------------- PROFILE ---------------- #

def save_profile(name, branch, cgpa, skills):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO profile(name, branch, cgpa, skills)
        VALUES (?, ?, ?, ?)
        """,
        (name, branch, cgpa, skills)
    )

    conn.commit()

    conn.close()


def get_profiles():

    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM profile",
        conn
    )

    conn.close()

    return df


# ---------------- PLACEMENT TRACKER ---------------- #

def add_application(company_name, role, status):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO companies(company_name, role, status)
        VALUES (?, ?, ?)
        """,
        (company_name, role, status)
    )

    conn.commit()

    conn.close()


def get_companies():

    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM companies",
        conn
    )

    conn.close()

    return df


def update_application(application_id, new_status):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE companies
        SET status = ?
        WHERE id = ?
        """,
        (new_status, application_id)
    )

    conn.commit()

    conn.close()


def delete_application(delete_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM companies
        WHERE id = ?
        """,
        (delete_id,)
    )

    conn.commit()

    conn.close()


# ---------------- STATISTICS ---------------- #

def get_application_statistics():

    df = get_companies()

    total = len(df)

    applied_count = len(
        df[df["status"] == "Applied"]
    )

    interview_count = len(
        df[df["status"] == "Interview"]
    )

    selected_count = len(
        df[df["status"] == "Selected"]
    )

    rejected_count = len(
        df[df["status"] == "Rejected"]
    )

    return (
        total,
        applied_count,
        interview_count,
        selected_count,
        rejected_count
    )