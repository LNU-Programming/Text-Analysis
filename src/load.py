import os
import analyse


def load_file() -> dict[str, any]:
    # TODO: CAREFUL. The path should be relative to the current file, right now it's relative to where you execute the file!
    path = "../data/"
    print("\n--- File Selection ---\nAvailable text files:")
    try:
        for index, x in enumerate(os.listdir(path)):
            if x.endswith(".txt"):
                print(f"{index + 1}) {x}")
    except FileNotFoundError:
        print("File or directory not found.")
        return {"filename": ""}

    try:
        choice = int(input("Enter a number from the list above. "))
        # TODO: add possibility to type filename aswell
        selected_files = os.listdir("../data/")
        if 0 < choice <= len(selected_files):
            print(f"\nAnalyzing {selected_files[choice - 1]}...")
            return analyse.analyse_file(path, selected_files[choice - 1])
        print(f"Please enter a number between 1 and {len(selected_files)}")
        return load_file()
    except ValueError:
        print("Invalid input!")
        return load_file()
