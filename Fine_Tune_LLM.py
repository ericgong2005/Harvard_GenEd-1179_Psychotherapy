import google.generativeai as genai
import os
from dotenv import load_dotenv

import pandas as pd
import seaborn as sns
import time
import json

TRAINING_DATA_FILE = "training_data.jsonl"

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

base_model = "models/gemini-1.5-flash-001-tuning"

training_data = []
with open(TRAINING_DATA_FILE, 'r') as file:
    for line in file:
        entry = json.loads(line)
        training_data.append(entry)

operation = genai.create_tuned_model(
    display_name="increment",
    source_model=base_model,
    epoch_count=20,
    batch_size=4,
    learning_rate=0.001,
    training_data=training_data,
)

for status in operation.wait_bar():
    time.sleep(10)

result = operation.result()
print(result)

snapshots = pd.DataFrame(result.tuning_task.snapshots)
sns.lineplot(data=snapshots, x='epoch', y='mean_loss')

model = genai.GenerativeModel(model_name=result.name)
result = model.generate_content("III")
print(result.text)  # IV