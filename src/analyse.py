def analyse_file(path: str, filename: str) -> dict:
    statistics = {"filename": filename,
                  'total_lines': 0,
                  "total_words": 0,
                  "total_characters_with_spaces": 0,
                  "total_characters_without_spaces": 0,
                  "avg_words_per_line": 0.0,
                  "avg_char_per_word": 0.0,
                  "most_common_words": {}}
    all_words = {}

    try: # TODO: Refactor!
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
                            if temp_word in all_words:
                                all_words[temp_word] += 1
                            else:
                                all_words[temp_word] = 1
                        temp_word = ''

                statistics['total_lines'] += 1

            statistics['avg_words_per_line'] = statistics['total_words'] / statistics['total_lines']
            statistics['avg_char_per_word'] = statistics['total_characters_without_spaces'] / statistics['total_words']
            statistics['most_common_words'] = most_common_words(all_words)

    except FileNotFoundError:
        print("File not found.")

    return statistics

def most_common_words(all_words: dict) -> dict:
    top_ten_words = {}
    for _ in range(10):
        max_val = max(all_words, key=all_words.get)
        top_ten_words[max_val] = all_words[max_val]
        all_words.pop(max_val)

    return top_ten_words