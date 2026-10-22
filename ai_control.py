from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classify_request(user_input):
    pass

def handle_ai_request(user_input):
    # 1. Answer a question or chat
    # 2. perform a task that it can do (like open an app, type text, etc. or series (like a workflow in future))
    # 3. Clarify an unclear request or unknown request
    route = classify_request(user_input)

    if route == 1:
        answer_question(user_input)
    elif route == 2:
        perform_task(user_input)
    elif route == 3:
        ask_for_clarification(user_input)
