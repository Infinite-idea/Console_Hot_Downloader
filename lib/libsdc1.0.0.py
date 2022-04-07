# Import libraries
from pathlib import Path as path

# Main function
def CreateDirectory(DirAddress):
    # Set output directory
    output_dir = path(DirAddress)

    # Check if output directory is not exist create new one
    output_dir.mkdir(parents=True, exist_ok=True)