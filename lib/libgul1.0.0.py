# Import libraries
from pathlib import Path as path

# Main function
def __main__(FileAddress):
    try:
        # Open and read urls list file
        Urls = open(FileAddress).read().splitlines()

        # Return urls list
        return Urls
    except Exception as e:
        # Get error message
        ExcMsg = "Err on: [" + str(path(__file__).name) + "]"

        # Return error message
        return ExcMsg