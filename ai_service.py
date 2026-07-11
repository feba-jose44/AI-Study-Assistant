import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Read API key
API_KEY = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=API_KEY)


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

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text