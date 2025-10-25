def analyse_file(path: str, filename: str) -> dict:
    statistics = {"filename": filename, 'counter': 0}

    try:
        with open(f"{path}{filename}", "r") as file:
            for line in file:
                statistics['counter'] += 1
    except FileNotFoundError:
        print("File not found.")

    return statistics
