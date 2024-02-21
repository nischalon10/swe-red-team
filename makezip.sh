#!/bin/bash

# Specify the files to include
INCLUDE=("incollege.py" "main.py" "main.py" "README.md" "requirements.txt" "test_incollege_app.py" ".gitignore")

# Create the zip command with inclusions
ZIP_CMD="zip swe-red-team.zip"
for FILE in "${INCLUDE[@]}"; do
    ZIP_CMD="${ZIP_CMD} ${FILE}"
done

# Execute the zip command
eval $ZIP_CMD