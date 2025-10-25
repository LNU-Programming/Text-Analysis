def analyse_file(path: str, filename: str) -> dict:
    statistics = {"filename": filename,
                  'total_lines': 0,
                  "total_words": 0,
                  "total_characters_with_spaces": 0,
                  "total_characters_without_spaces": 0,
                  "avg_words_per_line": 0.0,
                  "avg_char_per_word": 0.0}

    try:
        with open(f"{path}{filename}", "r") as file:
            temp_word = ''
            for line in file:
                for char in line:
                    statistics['total_characters_with_spaces'] += 1
                    if char.isalpha():
                        temp_word += char.lower()
                    else:
                        if temp_word != '':
                            statistics['total_words'] += 1
                            statistics['total_characters_without_spaces'] += len(temp_word)
                            if temp_word in statistics:
                                statistics[temp_word] += 1
                            else:
                                statistics[temp_word] = 1
                        temp_word = ''

                statistics['total_lines'] += 1

            statistics['avg_words_per_line'] = statistics['total_words'] / statistics['total_lines']
            statistics['avg_char_per_word'] = statistics['total_characters_without_spaces'] / statistics['total_words']

    except FileNotFoundError:
        print("File not found.")

    return statistics