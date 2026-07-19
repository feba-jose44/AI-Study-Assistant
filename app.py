import streamlit as st
from pdf_reader import read_pdf
from ai_service import generate_quiz, summarize, answer_question, translate_notes

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
st.header("🤖 AI Study Assistant")
st.write("Upload your study notes and let the AI help you summarize, generate quizzes, answer questions, and translate your notes into different languages.")

st.divider()
st.header("Choose an Action")
# -------------------------------
# File Upload
# -------------------------------
st.sidebar.title("🤖 AI Study Assistant")
uploaded_file = st.sidebar.file_uploader(
    "Upload your study notes",
    type=["pdf"]
)
if uploaded_file:
    st.sidebar.success("✅PDF uploaded successfully!")
    st.sidebar.write(f"**File:** {uploaded_file.name}")
st.sidebar.markdown("""
### How to use

1. Upload a PDF.
2. Wait for the text to be extracted.
3. Choose one of the AI features.
4. View the generated result.
""")
all_text = ""
if uploaded_file is not None:
    all_text = read_pdf(uploaded_file)

# -------------------------------
# Read PDF
# -------------------------------

st.divider()

# -------------------------------
# Helper Function
# -------------------------------
# -------------------------------
# Buttons
# -------------------------------


with st.expander("📝 Summarize Notes"):
    if st.button("Generate Summary"):
        if uploaded_file is None:
             st.warning("Please upload a file first.")
        else:
            with st.spinner("Generating summary..."):
                summary = summarize(all_text)
            st.success("Summary generated successfully!")
            st.subheader("Summary")
            st.text_area(
                "AI Summary",
                summary,
                height=200
                )

with st.expander("❓ Generate Quiz"):
    if st.button("Generate Quiz"):
        if uploaded_file is None:
            st.warning("Please upload a file first.")
        else:
            with st.spinner("Generating quiz..."):
                quiz = generate_quiz(all_text)
            st.success("Quiz generated successfully!")
            st.subheader("Quiz")
            st.text_area(
                "AI Generated Quiz",
                quiz,
                height=400
            )

with st.expander("💬 Ask Questions"):
    question = st.text_input("Ask a question about your notes:")
    if st.button("Ask Questions"):
        if uploaded_file is None:
            st.warning("Please upload a file first.")
        elif not question:
            st.warning("Please enter a question.")
        else:
            with st.spinner("Generating answer..."):
                answer = answer_question(all_text, question)
            st.success("Answer generated successfully!")
            st.subheader("Answer")
            st.text_area(
                "AI Answer",
                answer,
                height=200
            )
with st.expander("🌍 Translate Notes"):
    language = st.selectbox(
        "Select a language for translation:",
        ("English", "Hindi", "Telugu","Spanish", "French", "German", "Chinese")
    )
    if st.button("Translate Notes"):
        if uploaded_file is None:
            st.warning("Please upload a file first.")
        else:
            with st.spinner("Translating notes..."):
                translation = translate_notes(all_text, language)
            st.success("Translation completed successfully!")
            st.subheader(f"Translated Notes ({language})")
            st.text_area(
                "AI Translated Notes",
                translation,
                height=300
            )



# -------------------------------
# Output
# -------------------------------
with st.expander("📄Preview Uploaded Notes"):
    if all_text:
        st.text_area(
            "PDF Content",
            all_text,
            height=300
        )
    else:
        st.info("Upload a PDF to view its extracted text here.")
st.divider()
st.caption(
    "Built using Streamlit and Gemini API. © 2026 AI Study Assistant"
)
