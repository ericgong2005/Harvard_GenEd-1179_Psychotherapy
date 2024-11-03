import google.generativeai as genai
from dotenv import load_dotenv
import os
import json

INPUT_FILE = "questions.jsonl"

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

question_list = []

with open(INPUT_FILE, 'r') as file:
    for line in file:
        question_list.append(json.loads(line.strip()))

model = genai.GenerativeModel("gemini-1.5-flash")

for question in question_list:
    response = model.generate_content(question["Prompt"])
    print(response.text)