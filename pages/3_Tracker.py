import streamlit as st
import sqlite3
import os
import pandas as pd

# Set page config for a wide layout
st.set_page_config(page_title="Tracker", layout="wide")


def apply_custom_css():
    try:
        with open("style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass


def get_all_submissions():
    """Fetch all records from the SQLite database."""
    try:
        conn = sqlite3.connect("submissions.db")
        # Converting to a DataFrame for easier handling
        df = pd.read_sql_query("SELECT id, path, submitter, status FROM submissions", conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Database error: {e}")
        return pd.DataFrame()


def get_status_color(status):
    """Returns a CSS style based on the status."""
    colors = {
        "Pending": "background-color: #f0f0f0; color: #666; border: 1px solid #ccc;",
        "In Progress": "background-color: #fff3cd; color: #856404; border: 1px solid #ffeeba;",
        "Interviewing": "background-color: #d1ecf1; color: #0c5460; border: 1px solid #bee5eb;",
        "Summary Generated": "background-color: #d4edda; color: #155724; border: 1px solid #c3e6cb;"
    }
    return colors.get(status, "background-color: #fff; color: #000;")


apply_custom_css()

st.title("📊 Workflow Status Tracker")
st.markdown("Monitor the progress of all document analyses and download final reports.")

# Fetch data
df = get_all_submissions()

if df.empty:
    st.info("No submissions found. Please approve documents in the Inbox first.")
else:
    # Header row
    st.divider()
    h1, h2, h3, h4 = st.columns([3, 2, 2, 2])
    h1.write("**File Path**")
    h2.write("**Submitter**")
    h3.write("**Current Status**")
    h4.write("**Actions**")
    st.divider()

    # Data rows
    for index, row in df.iterrows():
        c1, c2, c3, c4 = st.columns([3, 2, 2, 2])

        c1.text(row['path'])
        c2.text(row['submitter'])

        # Status Badge
        status = row['status']
        c3.markdown(
            f'<span style="padding: 4px 12px; border-radius: 12px; font-weight: bold; font-size: 0.85rem; {get_status_color(status)}">'
            f'{status}</span>',
            unsafe_allow_html=True
        )

        # Action Column (Download Logic)
        if status in ["Summary Generated", "Summary Generating", "✅ PowerPoint Ready!"]:
            file_path = f"exports/Strategic_Report_{row['id']}.pptx"
            if os.path.exists(file_path):
                with open(file_path, "rb") as f:
                    c4.download_button(
                        label="📥 Download PPTX",
                        data=f,
                        file_name=f"Summary_{row['submitter']}.pptx",
                        mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                        key=f"btn_{row['id']}"
                    )
            else:
                c4.warning("File not found")
        elif status == "Interviewing":
            c4.info("Live Interview")
        else:
            c4.write("---")

# Sidebar summary
st.sidebar.title("System Stats")
if not df.empty:
    st.sidebar.metric("Total Submissions", len(df))
    st.sidebar.metric("Completed", len(df[df['status'] == "Summary Generated"]))

st.sidebar.divider()
if st.sidebar.button("🔄 Refresh Data"):
    st.rerun()
