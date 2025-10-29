import os
import analyse


PATH = '../data/'
# Color codes
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"  # Reset to default color


def load_file() -> dict[str, any]:
    print("\n--- File Selection ---\nAvailable text files:")
    try:
        for index, x in enumerate(os.listdir(PATH)):
            if x.endswith(".txt"):
                print(f"{index + 1}) {x}")
    except FileNotFoundError:
        print(f"{RED}File or directory not found.{RESET}")
        return {"filename": ""}

    try:
        choice = input("Enter a number from the list above, or write the name of the file: ")
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
