"""
File loading module for text analysis application.

This module provides functionality to interactively select and load text files
from a designated data directory. It displays available .txt files to the user,
accepts their selection via index or filename, and delegates the file analysis
to the analyse module.
"""

import os
import analyse


PATH = '../data/'
# Color codes
BOLD = '\033[1m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
RESET = '\033[0m'


def load_file() -> dict[str, any]:
    """
    Interactively load and analyze a text file from the data directory.

    This function displays all available .txt files in the PATH directory,
    prompts the user to select a file either by entering its index number
    or full filename, and then passes the selected file to the analyse module
    for processing.

    The function handles various error cases:
    - FileNotFoundError: If the data directory doesn't exist
    - ValueError: If the user enters invalid input (non-numeric when expected)
    - Invalid selection: If the user enters an index out of range

    If an error occurs or invalid input is provided, the function recursively
    calls itself to prompt the user again.

    Returns:
        dict[str, any]: A dictionary containing the analysis results from
            analyse.analyse_file().
    """
    print(f"\n{BOLD}--- File Selection ---\nAvailable text files:{RESET}")
    try:
        for index, x in enumerate(os.listdir(PATH)):
            if x.endswith(".txt"):
                print(f"{ITALIC}{index + 1}) {x}{RESET}")
    except FileNotFoundError:
        print(f"{RED}File or directory not found.{RESET}")
        return {"filename": ""}

    try:
        choice = input("\nEnter index or filename: ")
        selected_files = os.listdir(PATH)

        if choice.endswith('.txt') and choice in selected_files:
            return analyse.analyse_file(PATH, choice)
        else:
            if 0 < int(choice) <= len(selected_files):
                print(f"\nAnalyzing {selected_files[int(choice) - 1]}...")
                return analyse.analyse_file(PATH, selected_files[int(choice) - 1])
        print(f"{RED}Please enter a number between 1 and {len(selected_files)}{RESET}")
        return load_file()
    except ValueError:
        print(f"{RED}Invalid input!{RESET}")
        return load_file()
