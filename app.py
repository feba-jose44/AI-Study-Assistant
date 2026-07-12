import streamlit as st
from pdf_reader import read_pdf
from ai_service import generate_quiz, summarize 

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🤖",
    layout="wide"
)

# -------------------------------
# Title
# -------------------------------
st.title("🤖 AI Study Assistant")
st.write("Welcome! Upload your study notes and let AI help you learn.")

st.divider()

# -------------------------------
# File Upload
# -------------------------------
uploaded_file = st.file_uploader(
    "Upload your study notes",
    type=["pdf", "txt", "docx"]
)

# -------------------------------
# Read PDF
# -------------------------------
all_text = ""

if uploaded_file is not None:

    st.success(f"Successfully uploaded: {uploaded_file.name}")

    # Read PDF only if the uploaded file is a PDF
    if uploaded_file.type == "application/pdf":

        all_text = read_pdf(uploaded_file)

st.divider()

# -------------------------------
# Helper Function
# -------------------------------
def perform_action(action_name):
    if uploaded_file is None:
        st.warning("Please upload a file first.")
    else:
        st.success(f"{action_name}...")

# -------------------------------
# Buttons
# -------------------------------
st.subheader("Choose an Action")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📝 Generate Summary"):
        if uploaded_file is None:
            st.warning("Please upload a file first.")
        else:
            summary = summarize(all_text)
            st.subheader("Summary")
            st.text_area(
                "AI Summary",
                summary,
                height=200
            )

            st.write(summary)

with col2:
    if st.button("❓ Generate Quiz"):
        if uploaded_file is None:
            st.warning("Please upload a file first.")
        else:
            quiz = generate_quiz(all_text)
            st.subheader("Quiz")
            st.text_area(
                "AI Generated Quiz",
                quiz,
                height=400
            )

with col3:
    if st.button("💬 Ask Questions"):
        perform_action("Opening Q&A")

if st.button("🌍 Translate Notes"):
    perform_action("Translating notes")

st.divider()

# -------------------------------
# Output
# -------------------------------
st.subheader("Extracted Text")

if all_text:
    st.text_area(
        "PDF Content",
        all_text,
        height=300
    )
else:
    st.info("Upload a PDF to view its extracted text here.")