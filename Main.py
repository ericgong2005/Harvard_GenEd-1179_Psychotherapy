'''
Main.py provides driver code that unifies the functionalities of Parse_Data.py,
Fine_Tune_LLM.py and Query_LLM.py
'''

import sys

from Parse_Data import parse
from Fine_Tune_LLM import finetune
from Query_LLM import query

VALID_COMMANDS = ["help", "-p", "-f", "-q", "-a"]

HELP_STRING = "Commands:\n\t-p:\tParse vignettes and populate the tuning and querying files\n\t-f:\tFinetune an LLM model for querying\n\t-q:\tQuery the LLM\n\t-a:\tAll of the above"

def main():
    if len(sys.argv) != 2:
        sys.exit("Incorrect Usage. Use \"Main help\" to learn more")
    
    command = sys.argv[1]
    if command not in VALID_COMMANDS:
        sys.exit("Incorrect Usage. Use \"Main help\" to learn more")

    if command == "help":
        print(HELP_STRING)
    if command == "-p" or command == "-a":
        print("Extracting Vignettes")
        parse()
    if command == "-f" or command == "-a":
        print("Finetuning Model")
        finetune()
    if command == "-q" or command == "-a":
        print("Querying Model")
        query()

if __name__ == '__main__':
    main()