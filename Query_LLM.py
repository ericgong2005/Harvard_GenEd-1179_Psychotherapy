'''
Query_LLM.py queries the fine-tuned LLM model TUNED_MODEL with queries 
specified in QUERY_FILE, writing the results to OUTPUT_FILE as specified
in the config.yaml
'''

from dotenv import load_dotenv
import google.generativeai as genai
import os
import json
import asyncio

from helpers import get_config

async def query_llm(question_list : list[str], config : dict):
    genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
    
    model = genai.GenerativeModel(model_name=config["TUNED_MODEL"])
    
    for question in question_list:
        result = model.generate_content(question["Prompt"])
        with open(config["OUTPUT_FILE"], mode='a') as f:
            f.write(json.dumps({
                "Vignette": question["Vignette"],
                "Response": result.text,
                "Answer": question["Answer"]
            }) + '\n')

def query() :
    load_dotenv()

    config = get_config()

    question_list = []

    with open(config["QUERY_FILE"], 'r') as file:
        for line in file:
            entry = json.loads(line.strip())
            formatted_entry = {"Prompt": config["PROMPT"] + "\n" + entry["Description"], 
                               "Vignette" : entry["Vignette"],
                               "Answer": entry["Diagnosis"]}
            question_list.append(formatted_entry)

    asyncio.run(query_llm(question_list, config))

if __name__ == '__main__':
    query()