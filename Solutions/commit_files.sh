#!/bin/bash

# Loop through each Python file in the current directory
for file in *.py; do
    # Add the file to the staging area
    git add "$file"
    
    # Commit the file with the commit message as the file name
    git commit -m "$file"
done

# Give the script execute permissions with the command chmod +x commit_files.sh
# Run the script with ./commit_files.sh