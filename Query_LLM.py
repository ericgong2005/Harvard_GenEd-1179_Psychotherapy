from dotenv import load_dotenv
import google.generativeai as genai
import os
import json
import asyncio

INPUT_FILE = "questions.jsonl"

OUTPUT_FILE = "response.jsonl"

async def query_llm(question_list : list[str]):
    genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
    
    model = genai.GenerativeModel(model_name="tunedModels/test-rghw9g8zz717")
    for question in question_list:
        result = model.generate_content(question["Prompt"])
        with open(OUTPUT_FILE, mode='a') as f:
            f.write(json.dumps({
                'response': result.text
            }) + '\n')


def main() :
    load_dotenv()

    question_list = []

    with open(INPUT_FILE, 'r') as file:
        for line in file:
            question_list.append(json.loads(line.strip()))

    asyncio.run(query_llm(question_list))

if __name__ == '__main__':
    main()