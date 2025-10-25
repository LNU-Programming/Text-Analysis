import os
import analyse

def load_file() -> dict:
    print("\n--- File Selection ---\nAvailable text files:")
    try:
        for index, x in enumerate(os.listdir('../data/')):
            if x.endswith(".txt"):
                print(f'{index+1}) {x}')
    except FileNotFoundError:
        print("File or directory not found.")
        return None

    try:
        choice = int(input("Enter a number from the list above. "))
        selected_files = os.listdir('../data/')
        if 0 < choice <= len(selected_files):
            return analyse.analyse_file(selected_files[choice - 1])
        print(f"Please enter a number between 1 and {len(selected_files)}")
        return load_file()
    except ValueError:
        print("Invalid input!")
        return load_file()