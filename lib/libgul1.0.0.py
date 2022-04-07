# Import libraries
from pathlib import Path as path

# Main function
def __main__(FileAddress):
    try:
        Urls = open(FileAddress).read().splitlines()
        return Urls
    except Exception as e:
        ExcMsg = "Err on: [" + str(path(__file__).name) + "]"
        return ExcMsg