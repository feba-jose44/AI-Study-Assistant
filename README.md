# 🤖 AI Study Assistant

An AI-powered Study Assistant built with **Python**, **Streamlit**, and the **Google Gemini API**. This application helps students study more efficiently by summarizing notes, generating quizzes, answering questions from uploaded notes, and translating study material into multiple languages.

---

## 📌 Features

- 📄 Upload PDF study notes
- 📝 AI-generated summaries
- ❓ Automatic quiz generation
- 💬 Ask questions based on your uploaded notes
- 🌍 Translate notes into multiple languages
- ⏳ Loading indicators for AI tasks
- ✅ Success messages and error handling
- 📖 Preview extracted text from uploaded PDF

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- PyPDF2
- python-dotenv

---

## 📂 Project Structure

```
AI-Study-Assistant/
│
├── app.py                 # Main Streamlit application
├── ai_service.py          # Gemini API integration
├── pdf_reader.py          # PDF text extraction
├── requirements.txt       # Project dependencies
├── .env                   # API key (not uploaded to GitHub)
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/AI-Study-Assistant.git
cd AI-Study-Assistant
```

### 2. Create a virtual environment (Optional)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Create a file named `.env` in the project directory.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🚀 How to Use

1. Upload a PDF containing your study notes.
2. Wait for the notes to be processed.
3. Choose one of the available AI features:
   - Generate Summary
   - Generate Quiz
   - Ask Questions
   - Translate Notes
4. View the generated output.

---

## 🌍 Supported Translation Languages

- English
- Hindi
- Telugu
- Spanish
- French
- German
- Chinese

---

## 📸 Screenshots

### Home Page

> Add a screenshot here.

### Summary Generation

> Add a screenshot here.

### Quiz Generation

> Add a screenshot here.

### Ask Questions

> Add a screenshot here.

### Translation

> Add a screenshot here.

---

## 🔒 Environment Variables

This project uses the Google Gemini API.

Your API key is stored securely in a `.env` file and is **not** committed to GitHub.

---

## 🎯 Future Improvements

- 📚 AI Flashcards
- 📄 Export summaries as PDF
- 🔊 Text-to-Speech
- 📑 Support multiple PDFs
- 💾 Save previous sessions
- ☁️ Cloud deployment

---

## 👨‍💻 Author

**Feba Jose**

B.Tech Computer Science Engineering  
CMR College of Engineering & Technology

---

## ⭐ Acknowledgements

- Streamlit
- Google Gemini API
- PyPDF2

---

If you found this project helpful, consider giving it a ⭐ on GitHub!