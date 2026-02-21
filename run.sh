#!/bin/bash 

pandoc -t gfm --extract-media . "main.docx" -o main.md

# Run the Python replacement script 
python replace.py

# Delete the file main.md
python delete_file.py