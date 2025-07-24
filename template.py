import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(message)s:')

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "research/trails.ipynb",
    "setup.py",  # Ensure these are here
    "app.py"     # Ensure these are here
]

for filepath in list_of_files:
    # Use pathlib for robust path handling
    path_obj = Path(filepath)
    filedir = path_obj.parent
    filename = path_obj.name

    # Create directory if it doesn't exist
    if filedir: # Check if filedir is not empty (i.e., it's a subdirectory)
        logging.info(f"Checking/Creating directory: {filedir}")
        os.makedirs(filedir, exist_ok=True)
    
    # Check if file exists or is empty, then create/touch it
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            pass # Create empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filepath} is already exists")