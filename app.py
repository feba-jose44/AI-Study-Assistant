import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 AI Study Assistant")

st.write("Welcome! Upload your study notes and let AI help you learn.")

st.divider()

# File uploader
uploaded_file = st.file_uploader(
    "Upload your study notes",
    type=["pdf", "txt", "docx"]
)

st.divider()

st.subheader("Choose an Action")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📝 Generate Summary"):
        if uploaded_file is None:
            st.warning("Please upload a file first.")
        else:
            st.success("Generating summary...")

with col2:
    if st.button("❓ Generate Quiz"):
        if uploaded_file is None:
            st.warning("Please upload a file first.")
        else:
            st.write("Generating quiz...")

with col3:
    if st.button("💬 Ask Questions"):
        if uploaded_file is None:
            st.warning("Please upload a file first.")
        else:
            st.write("Opening Q&A...")
st.divider()

st.subheader("Output")

st.info("Your AI results will appear here.")