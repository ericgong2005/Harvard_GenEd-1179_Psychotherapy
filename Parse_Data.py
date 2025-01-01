'''
Parse_Data.py populates the jsonl files TUNING_FILE and QUERY_FILE by formatting
the Clinical Vignettes found in TUNING_VIGNETTE and QUERY_VIGNETTE respectively
with the files defined in config.yaml
'''

import re
import json
from PyPDF2 import PdfReader

from helpers import get_config

def extract_vignettes(vignette_path, output_path):
    reader = PdfReader(vignette_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    
    match = re.search(r'Contents(.*?)(\n\n)', text, re.DOTALL)
    
    vignette_names = match.group(1)
    
    vignette_name_list = []
    for line in vignette_names.splitlines():
        stripped_line = line.strip()
        if stripped_line:
            vignette_name_list.append(stripped_line)
        else:
            break
    
    results = []

    for index, vignette in enumerate(vignette_name_list):
        pattern = re.compile(
            rf"Case {index}\s+{re.escape(vignette)}\s+HISTORY(.*?)DIAGNOSTIC IMPRESSIONS(.*?)DIAGNOSTIC CONCLUSIONS(.*?)SUGGESTED THERAPEUTIC INTERVENTIONS(.*?)(?=Case|$)",
            re.DOTALL
        )
        match = pattern.search(text)
        
        if match:
            history = match.group(1).strip()
            diagnostic_impressions = match.group(2).strip()
            diagnostic_conclusions = match.group(3).strip()
            therapeutic_interventions = match.group(4).strip()
            
            vignette_data = {
                "Vignette": vignette,
                "Description": history,
                "Diagnostic Impressions": diagnostic_impressions,
                "Diagnosis": diagnostic_conclusions,
                "Interventions": therapeutic_interventions
            }
            results.append(vignette_data)
    
    with open(output_path, 'w') as outfile:
        for result in results:
            outfile.write(json.dumps(result) + '\n')

def parse():
    config = get_config()
    extract_vignettes(config["TUNING_VIGNETTE"], config["TUNING_FILE"])
    extract_vignettes(config["QUERY_VIGNETTE"], config["QUERY_FILE"])
    
if __name__ == '__main__':
    parse()
