import streamlit as st
import os
from database import save_answer

st.set_page_config(page_title="Conversation", layout="wide")

# Purple Palette for the UI
PURPLE_DEEP = "#4B2680"
PURPLE_LIGHT = "#A081D7"

# Visual Impact Scale with Smiley Faces
impact_map = {
    0: "😶",
    1: "🤨",
    2: "😐",
    3: "🙂",
    4: "🤩"
}

st.title("💬 Conversation with sushmita.bhamidipati")

with st.form("client_feedback_form"):
    # --- SECTION 1: NARRATIVE RESONANCE ---
    st.subheader("1. How did the differentiated client narrative resonate with the client?")
    q1 = st.select_slider(
        " ",
        options=[0, 1, 2, 3, 4],
        format_func=lambda x: impact_map[x],
        key="resonate_slider"
    )

    st.divider()

    # --- SECTION 2: OFFERINGS & SOLUTIONS ---
    st.subheader("2. What were the most relevant Offerings and Solutions for your client conversation?")
    off1 = st.select_slider("CGS, Retail & Travel Core Value Chain / Marketing Transformation",
                        options=[0, 1, 2, 3, 4], format_func=lambda x: impact_map[x])
    off2 = st.select_slider("Marketing / Marketing Transformation", options=[0, 1, 2, 3, 4],
                        format_func=lambda x: impact_map[x])
    off3 = st.select_slider("Marketing / Intelligent Marketing Performance", options=[0, 1, 2, 3, 4],
                        format_func=lambda x: impact_map[x])
    off4 = st.select_slider("Marketing / Marketing Content Activation", options=[0, 1, 2, 3, 4],
                        format_func=lambda x: impact_map[x])
    off5 = st.select_slider("AI & Data Platforms / Advanced AI", options=[0, 1, 2, 3, 4],
                            format_func=lambda x: impact_map[x])
    off6 = st.select_slider("AI & Data Platforms / Intelligent Marketing Performance", options=[0, 1, 2, 3, 4],
                            format_func=lambda x: impact_map[x])
    off7 = st.select_slider("AI & Data Platforms / Marketing Content Activation", options=[0, 1, 2, 3, 4],
                            format_func=lambda x: impact_map[x])
    st.divider()

    # --- SECTION 3: PRODUCTS & PLATFORMS ---
    st.subheader("3. Which were the most relevant Products and Platform for your client conversation?")
    p1 = st.select_slider("AI Refinery", options=[0, 1, 2, 3, 4], format_func=lambda x: impact_map[x])
    p2 = st.select_slider("Attribution Platform", options=[0, 1, 2, 3, 4], format_func=lambda x: impact_map[x])
    p3 = st.select_slider("Accenture Multimedia Services", options=[0, 1, 2, 3, 4], format_func=lambda x: impact_map[x])
    p4 = st.select_slider("Accenture Momentum (Vision to value)", options=[0, 1, 2, 3, 4],
                          format_func=lambda x: impact_map[x])
    p5 = st.select_slider("SynOps for Marketing Operations", options=[0, 1, 2, 3, 4],
                          format_func=lambda x: impact_map[x])

    st.divider()

    # --- SECTION 4: CLIENT PERSONAS ---
    st.subheader("4. Which Client Personas did you engage with?")
    per1 = st.select_slider("Chief Marketing Officer", options=[0, 1, 2, 3, 4], format_func=lambda x: impact_map[x])
    per2 = st.select_slider("Chief Technology Officer", options=[0, 1, 2, 3, 4],
                                format_func=lambda x: impact_map[x])
    per3 = st.select_slider("Chief Transformation Officer", options=[0, 1, 2, 3, 4],
                                format_func=lambda x: impact_map[x])
    per4 = st.select_slider("Chief Executive Officer", options=[0, 1, 2, 3, 4], format_func=lambda x: impact_map[x])
    per5 = st.select_slider("Chief Information Officer", options=[0, 1, 2, 3, 4],
                            format_func=lambda x: impact_map[x])
    per6 = st.select_slider("Chief Data & AI Officer", options=[0, 1, 2, 3, 4], format_func=lambda x: impact_map[x])
    per7 = st.select_slider("Global Business Services Lead", options=[0, 1, 2, 3, 4],
                            format_func=lambda x: impact_map[x])

    st.divider()

    # --- SECTION 5: OPEN FEEDBACK ---
    st.subheader("5. What were they most interested in and what other questions did they ask?")
    q5 = st.text_area(" ", height=150)

    # --- SUBMIT ---
    if st.form_submit_button("Submit", type="primary"):
        if "active_interview" in st.session_state:
            sub_id = st.session_state.active_interview['id']
            # Logic to save all these sliders to the DB...
            save_answer(sub_id, "Feedback_Narrative_Resonance", impact_map[q1])
            save_answer(sub_id, "Feedback_Qualitative", q5)
            st.success("✅ Feedback successfully logged. The Learning Loop has been updated.")
        else:
            st.error("No active session found to link this feedback.")

st.caption("Strategic Feedback Engine v1.0 | Powered by Contextual Intelligence")