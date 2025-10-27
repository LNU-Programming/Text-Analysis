SENTENCE_ENDERS = {".", "!", "?"}
WORD_BOUNDARIES = {" ", "\t", "\n", ",", ";", ":"}
TOP_WORDS_COUNT = 10


def analyse_file(path: str, filename: str) -> dict[str, any]:
    statistics = initialize_statistics(filename)
    analysis_data = initialize_analysis_data()

    try:
        with open(f"{path}{filename}", "r") as file:
            for line in file:
                process_line(line, statistics, analysis_data)

        finalize_remaining_data(statistics, analysis_data)
        calculate_final_statistics(statistics, analysis_data)
    except FileNotFoundError:
        print("File not found.")

    print(f"Analysis complete! Processed {statistics['total_lines']} lines.")
    print(f'Successfully loaded and analyzed "{statistics["filename"]}"')
    return statistics


def initialize_statistics(filename: str) -> dict[str, any]:
    return {
        "filename": filename,
        # ==== Basic statistics ====
        "total_lines": 0,
        "total_paragraphs": 0,  # TODO
        "total_sentences": 0,
        "total_words": 0,
        "total_characters_with_spaces": 0,
        "total_characters_without_spaces": 0,  # TODO
        "avg_words_per_line": 0.0,
        "avg_char_per_word": 0.0,
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


def initialize_analysis_data() -> dict[str, any]:
    return {  # Initialize the data structures used during analysis
        "all_words": {},
        "word_lengths": [0 for _ in range(45)],
        "sentence_lengths": [],
        "current_word": "",
        "current_sentence": ""
    }


def process_line(line: str, statistics: dict, analysis_data: dict) -> None:
    statistics["total_lines"] += 1

    for char in line:
        process_character(char, statistics, analysis_data)


def process_character(char: str, statistics: dict, analysis_data: dict) -> None:
    statistics["total_characters_with_spaces"] += 1

    analysis_data["current_sentence"] += char

    # Check if we are at the end of a sentence
    if char in SENTENCE_ENDERS:
        analysis_data["sentence_lengths"].append(len(analysis_data["current_sentence"]))
        analysis_data["current_sentence"] = ""
        statistics["total_sentences"] += 1

    # Check if we are at the end of a word
    if char.isalpha():
        analysis_data["current_word"] += char.lower()
    else:
        finalize_current_word(statistics, analysis_data)


def finalize_current_word(statistics: dict, analysis_data: dict) -> None:
    current_word = analysis_data["current_word"]
    if current_word:
        statistics["total_words"] += 1
        analysis_data["word_lengths"].append(len(current_word))

        # Update word frequency
        if current_word in analysis_data["all_words"]:
            analysis_data["all_words"][current_word] += 1
        else:
            analysis_data["all_words"][current_word] = 1

        # Reset current word
        analysis_data["current_word"] = ""


def finalize_remaining_data(statistics: dict, analysis_data: dict) -> None:
    finalize_current_word(statistics, analysis_data)

    # Finalize current sentence if it exists, it might not be ending with punctuation
    if analysis_data["current_sentence"]:
        analysis_data["sentence_lengths"].append(len(analysis_data["current_sentence"]))
        statistics["total_sentences"] += 1


def calculate_final_statistics(statistics: dict, analysis_data: dict) -> None:
    if statistics["total_lines"] > 0:
        statistics["avg_words_per_line"] = (
            statistics["total_words"] / statistics["total_lines"]
        )

    if statistics["total_words"] > 0:
        statistics["avg_char_per_word"] = (
            statistics["total_characters_without_spaces"] / statistics["total_words"]
        )

    statistics["ten_most_common_words"] = most_common_words(analysis_data["all_words"])


def most_common_words(all_words: dict) -> dict:
    top_words = {}
    for _ in range(TOP_WORDS_COUNT):
        if not all_words:
            break
        max_val = max(all_words, key=all_words.get)
        top_words[max_val] = all_words[max_val]
        all_words.pop(max_val)

    return top_words


# Returns the length of the list, only counting elements different from 0
def list_true_length(word_len_lst: list) -> int:
    true_length = 0
    for element in word_len_lst:
        if element != 0:
            true_length += 1

    return true_length
