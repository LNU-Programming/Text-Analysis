def analyse_file(path: str, filename: str) -> dict[str, any]:
    statistics = {
        "filename": filename,
        # ==== Basic statistics ====
        "total_lines": 0,
        "total_paragraphs": 0,  # TODO
        "total_sentences": 0,  # TODO
        "total_words": 0,
        "total_characters_with_spaces": 0,
        "total_characters_without_spaces": 0,  # TODO
        "avg_words_per_line": 0.0,
        "avg_words_per_sentence": 0.0,  # TODO
        "avg_char_per_word": 0.0,  # TODO
        # ==== Word analysis ====
        "ten_most_common_words": {},
        "shortest_word": "",
        "longest_word": "",
        "avg_word_length": 0.0,
        "word_length_distribution": [],
        "unique_word_count": 0,
        "words_appearing_only_once": 0,
        # ==== Sentence analysis ====
        "average_words_per_sentence": 0.0,
        "longest_sentence": "",
        "shortest_sentence": "",
        "sentence_length_distribution": [],
        # ==== Character analysis ====
        "total_letters": 0,
        "total_digits": 0,
        "total_spaces": 0,
        "total_punctuation": 0,
        "letter_frequency_distribution": [],
        "punctuation_distribution": [],
        "case_distribution": [],
    }

    all_words = {}
    word_length_lst = []
    sentence_length_lst = []

    try:  # TODO: Refactor!
        with open(f"{path}{filename}", "r") as file:
            temp_word = ""
            temp_sentence = ""
            for line in file:
                for char in line:
                    statistics["total_characters_with_spaces"] += 1
                    temp_sentence += char

                    if char == "." or char == "!" or char == "?":
                        sentence_length_lst.append(len(temp_sentence))
                        temp_sentence = ""

                    if char.isalpha():
                        temp_word += char.lower()
                    else:
                        if temp_word != "":
                            statistics["total_words"] += 1
                            word_length_lst.append(len(temp_word))
                            if temp_word in all_words:
                                all_words[temp_word] += 1
                            else:
                                all_words[temp_word] = 1
                        temp_word = ""

                statistics["total_lines"] += 1

            statistics["avg_words_per_line"] = (
                statistics["total_words"] / statistics["total_lines"]
            )
            statistics["avg_char_per_word"] = (
                statistics["total_characters_without_spaces"]
                / statistics["total_words"]
            )
            statistics["ten_most_common_words"] = most_common_words(all_words)

    except FileNotFoundError:
        print("File not found.")

    print(f"Analysis complete! Processed {statistics['total_lines']} lines.")
    print(f'Successfully loaded and analyzed "{statistics["filename"]}"')
    return statistics


def most_common_words(all_words: dict) -> dict:
    top_ten_words = {}
    for _ in range(10):
        max_val = max(all_words, key=all_words.get)
        top_ten_words[max_val] = all_words[max_val]
        all_words.pop(max_val)

    return top_ten_words
