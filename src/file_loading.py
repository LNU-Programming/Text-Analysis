import os

def file_loading():
    print("\n--- File Selection ---\nAvailable text files:")
    # TODO: If no files ar present, return nothing
    # TODO: Add try catch when reading a file, since it might raise an exception and we don't want that

    try:
        for index, x in enumerate(os.listdir('../data/')):
            if x.endswith(".txt"):
                print(f'{index+1}) {x}')
    except FileNotFoundError:
        print("File or directory not found.")
        return None

    try:
        choice = int(input("Enter a number from the list above. "))
        selected_file = os.listdir('../data/')
        if 0 < choice <= len(selected_file):
            # TODO: call file analysis from here, we are just returning the book right now
            return selected_file[choice - 1]
        print(f"Please enter a number between 1 and {len(selected_file)}")
        return file_loading()
    except ValueError:
        print("Invalid input!")
        return file_loading()