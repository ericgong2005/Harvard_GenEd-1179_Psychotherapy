# Final Project for Harvard's GenEd 1179: Psychotherapy

## Overview:
This code is written to aid the evaluation of LLMs for the purposes of Psychotherapy as part of the final project for Harvard's GenEd1179: Psychotherapy course.

To begin, run "Main.py help"

## Functionalities:

The code contains three main functionalities:
1. To process Clinical Vignette PDFs, formatting each patient case into a single entry within a Jsonl file for either tuning or testing (querying) the LLM. This is accomplished in Parse_Data.py
2. To fine tune an LLM model based on provided Clinical Vignettes and diagnoses. This is accomplished in Fine_Tune_LLM.py
3. To query an LLM model with Clinical Vignettes and retrieving the LLM's predicted diagnosis. This is accomplished in Query_LLM,py

The three functionalities are utilized through Main.py, and the config.yaml file is used to specify file paths and model names as needed for each of the functionalities.

Note that for copyright reasons, the PDF copies of the Clinical Vignettes, as well as the final Tuning, Querying, and Output files which contain parsed versions of the Clinical Vignettes, are not featured in this repository

## Results:
The results of the project, alongside a detailed motivation and methodology can be found in the Final_Paper.pdf, containing the paper submission for this project for the course.