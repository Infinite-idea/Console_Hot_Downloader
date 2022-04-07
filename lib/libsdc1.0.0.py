# Import libraries
from pathlib import Path as path

# Main function
def CreateStorage():
    # Set output directory
    output_dir = path('Storage')

    # Check if output directory is not exist create new one
    output_dir.mkdir(parents=True, exist_ok=True)
