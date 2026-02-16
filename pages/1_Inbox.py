import streamlit as st
import pandas as pd
import sqlite3
from database import approve_submission
# Import the new Architect utility
from architect_utils import generate_strategic_questions

st.set_page_config(
    page_title="Contextual Intelligence PoC",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Dummy data generator
def get_dummy_submissions():
    return [
        {"id": 1, "path": "docs/Bridging 6G IoT and AI.pdf", "submitter": "Aristhone Volkov", "contacts": "aristhone@company.cr",
         "status": "Pending"},
        {"id": 2, "path": "docs/neural_mesh_v4.pdf", "submitter": "Sienna Thorne", "contacts": "sienna@company.cr",
         "status": "Pending"},
        {"id": 3, "path": "docs/hydro_gen_zero.pdf", "submitter": "Mateo Chen", "contacts": "mat@company.cr",
         "status": "Pending"},
        {"id": 4, "path": "docs/m_and_a_v2.pdf", "submitter": "David Vega", "contacts": "david@company.cr",
         "status": "Pending"},
        {"id": 5, "path": "docs/orbital_debris.pdf", "submitter": "Elara Vance", "contacts": "vance@company.cr",
         "status": "Pending"},
    ]


st.title("📥 Inbox: Pending Approvals")
st.markdown("Select a document to initiate the AI-driven strategic conversation.")

# 1. Fetch current statuses from the database to check for existing approvals
def get_approved_ids():
    try:
        conn = sqlite3.connect("submissions.db")
        cursor = conn.cursor()
        # Fetch IDs where status is NOT 'Pending'
        cursor.execute("SELECT id FROM submissions WHERE status != 'Pending'")
        approved_ids = [row[0] for row in cursor.fetchall()]
        conn.close()
        return approved_ids
    except Exception:
        return []

approved_list = get_approved_ids()

# Display as a clean table
df = pd.DataFrame(get_dummy_submissions())

for index, row in df.iterrows():
    col1, col2, col3, col4 = st.columns([3, 2, 2, 1])

    is_already_approved = row['id'] in approved_list
    # Visual indicator for the user
    file_label = f"✅ {row['path']}" if is_already_approved else row['path']

    #col1.text(row['path'])
    col1.text(file_label)
    col2.text(row['submitter'])
    col3.text(row['contacts'])


    if col4.button("Approve", key=f"app_{row['id']}", disabled=is_already_approved):
        # 1. Start the Architect Agent Processing
        with st.status(f"🛠️ Architect Agent analyzing {row['path']}...", expanded=True) as status:
            try:
                st.write("Reading PDF content and identifying strategic drivers...")

                # 2. Call the Architect Agent (Generates 6 unique questions)
                # We pass the path and the filename
                dynamic_questions = generate_strategic_questions(row['path'], row['path'].split('/')[-1])

                st.write("✅ 6 Strategic questions generated successfully.")

                # 3. Add the Matrix Question at the beginning (Optional but recommended)
                #dynamic_questions.insert(0, "Matrix: Rate the impact (Low/Med/High) for AI, Data, Talent, and Methods.")

                # 4. Update the database status via your existing function
                approve_submission(row['id'], row['path'], row['submitter'])

                # 5. Set the active session state for the Interview page
                st.session_state.active_interview = {
                    "id": row['id'],
                    "user": row['submitter'],
                    "path": row['path'],
                    "questions": dynamic_questions
                }

                st.session_state.current_status = "Details Requested"

                status.update(label="Approval Complete!", state="complete", expanded=False)
                st.success(f"Analysis ready for {row['submitter']}! Go to the Conversation page.")

            except Exception as e:
                st.error(f"The Architect Agent encountered an error: {e}")
                status.update(label="Error in Analysis", state="error")
