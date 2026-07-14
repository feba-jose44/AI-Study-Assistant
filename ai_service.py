import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Read API key
API_KEY = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=API_KEY)

def ask_gemini(prompt):
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text

def summarize(text):

    prompt = f"""
    You are an expert study assistant.

    Summarize the following notes for a college student.

    Use:
    - Bullet points
    - Simple language
    - Keep important definitions
    - Maximum 250 words

    Notes:

    {text}
    """

    return ask_gemini(prompt)

def generate_quiz(text):

    prompt = f"""
    You are an expert study assistant.

    Based ONLY on the notes below, generate a quiz.

    Requirements:
    - 5 multiple-choice questions (4 options each)
    - 3 short-answer questions
    - 2 long-answer questions
    - Provide the correct answer after each question
    - Do not ask questions that are not covered in the notes
    - Format the quiz neatly using headings

    Notes:

    {text}
    """

    return ask_gemini(prompt)
def answer_question(text, question):

    prompt = f"""
    You are an expert study assistant.

    Answer the student's question using ONLY the uploaded notes.

    Requirements:
    - Answer in simple language
    - Use bullet points where appropriate
    - Explain in a detailed but easy-to-understand manner
    - If the answer is not present in the notes, clearly say:
      "This information is not available in the uploaded notes."
    - Do not make up information.

    Notes:
    {text}

    Question:
    {question}
    """

    return ask_gemini(prompt)