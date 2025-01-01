'''
Fine_Tune_LLM.py creates a fine-tuned LLM model from the specified PRETUNED_MODEL 
based on the example clinical vignettes provided by the TUNING_FILE, as specified 
in config.yaml, writing the final tuned model name to the config.yaml as TUNED_MODEL
'''

import google.generativeai as genai
import os
from dotenv import load_dotenv

import pandas as pd
import seaborn as sns
import time
import json

from helpers import get_config, set_config

def finetune():
    load_dotenv()

    config = get_config()
    
    genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

    base_model = config.get("PRETUNED_MODEL")

    tuning_data = []
    with open(config["TUNING_FILE"], 'r') as file:
        for line in file:
            entry = json.loads(line)
            formatted_entry = {"text_input": config["PROMPT"] + "\n" + entry["Description"], 
                               "output": entry["Diagnostic Impressions"] + "\n" + entry["Diagnosis"]}
            tuning_data.append(formatted_entry)

    operation = genai.create_tuned_model(
        display_name="increment",
        source_model=base_model,
        epoch_count=20,
        batch_size=4,
        learning_rate=0.001,
        training_data=tuning_data,
    )

    for status in operation.wait_bar():
        time.sleep(10)

    result = operation.result()
    print(result)

    snapshots = pd.DataFrame(result.tuning_task.snapshots)
    sns.lineplot(data=snapshots, x='epoch', y='mean_loss')

    model = genai.GenerativeModel(model_name=result.name)
    print(f"Tuned Model Name: {model}")

    config["TUNED_MODEL"] = model

    set_config(config)
            
if __name__ == '__main__':
    finetune()