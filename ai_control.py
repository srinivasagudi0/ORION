from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_ai_response(prompt):
    pass

def handle_ai_request(user_input):
    # let smallest AI pick what category the user input belongs to
    prompt = f"""

    """
