from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv
import os
import json
import asyncio

INPUT_FILE = "questions.jsonl"

OUTPUT_FILE = "response.jsonl"

async def query_llm(question_list : list[str]):
    model = ChatGoogleGenerativeAI(google_api_key=os.getenv('GOOGLE_API_KEY'), model="gemini-1.5-flash")

    for question in question_list:
        system_message = "You are a helpful assistant"
        user_message = question
        query_list = []
        query_list.append({"system": system_message, "user": user_message})
        prompt = ChatPromptTemplate.from_messages([("system", "{system}"),("human", "{user}"),])
        run = prompt | model
        responses = await run.abatch(query_list)
        count = 0
        for batch_item in responses:
            with open(OUTPUT_FILE, mode='a') as f:
                f.write(json.dumps({
                    'response': batch_item.dict()
                }) + '\n')
            count = count + 1


def main() :
    load_dotenv()

    question_list = []

    with open(INPUT_FILE, 'r') as file:
        for line in file:
            question_list.append(json.loads(line.strip()))

    asyncio.run(query_llm(question_list))

if __name__ == '__main__':
    main()