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
