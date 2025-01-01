'''
helpers.py contains the code that reads and writes the config.yaml
'''

import os
import sys
import yaml

CONFIG_FILE = "config.yaml"

EXPECTED_FIELDS = ["TUNING_FILE", "QUERY_FILE", "OUTPUT_FILE", "PRETUNED_MODEL", "TUNED_MODEL", "TUNING_VIGNETTE", "QUERY_VIGNETTE", "PROMPT"]

def get_config():
    if not os.path.exists(CONFIG_FILE):
        sys.exit("Error: Config file does not exist.")

    with open(CONFIG_FILE, 'r') as config_file:
        config = yaml.safe_load(config_file)
    
    for field in EXPECTED_FIELDS:
        if field not in config:
            sys.exit(f"Error: Config file missing {field}")

    return config
    
def set_config(config):
    if not os.path.exists(CONFIG_FILE):
        sys.exit("Error: Config file does not exist.")
    
    for field in EXPECTED_FIELDS:
        if field not in config:
            sys.exit(f"Error: Config file missing {field}")

    with open(CONFIG_FILE, 'w') as file:
        yaml.dump(config, file, default_flow_style=False)