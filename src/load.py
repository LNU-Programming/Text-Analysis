import os
import analyse

# Color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'  # Reset to default color
BOLD = '\033[1m'

def load_file() -> dict[str, any]:
    path = "../data/"
    print("\n--- File Selection ---\nAvailable text files:")
    try:
        for index, x in enumerate(os.listdir(path)):
            if x.endswith(".txt"):
                print(f"{index + 1}) {x}")
    except FileNotFoundError:
        print(f"{RED}File or directory not found.{RESET}")
        return {"filename": ""}

    try:
        choice = int(input("Enter a number from the list above. "))
        # TODO: add possibility to type filename aswell
        selected_files = os.listdir("../data/")
        if 0 < choice <= len(selected_files):
            print(f"\nAnalyzing {selected_files[choice - 1]}...")
            return analyse.analyse_file(path, selected_files[choice - 1])
        print(f"{RED}Please enter a number between 1 and {len(selected_files)}{RESET}")
        return load_file()
    except ValueError:
        print(f"{RED}Invalid input!{RESET}")
        return load_file()
