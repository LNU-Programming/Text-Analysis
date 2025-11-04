# Color codes
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"  # Reset to default color

SENTENCE_ENDERS = (".", "!", "?", ':--')
SENTENCE_EXCEPTIONS = ["dr", "mr", "st", "mrs", "ms", "inc", "ltd", "co", "corp", "llc", "plc", "u.s", "u.k", "e.u", "u.n", "ph.d", "e.g", "i.e", "etc"]
TOP_WORDS_COUNT = 10
PUNCTUATION = ('!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~')


def analyse_file(path: str, filename: str) -> dict[str, any]:
    statistics = initialize_statistics(filename)
    analysis_data = initialize_analysis_data()

    try:
        with open(f"{path}{filename}", "r", encoding='utf-8') as file:
            for line in file:
                process_line(line, statistics, analysis_data)

                if line.strip():
                    statistics['total_paragraphs'] += 1

        finalize_remaining_data(statistics, analysis_data)
        calculate_final_statistics(statistics, analysis_data)
    except FileNotFoundError:
        print("File not found.")

    print(f"{GREEN}Analysis complete! Processed {statistics['total_lines']} lines.{RESET}")
    print(f'{GREEN}Successfully loaded and analyzed "{statistics["filename"]}"{RESET}')
    return statistics


def initialize_statistics(filename: str) -> dict[str, any]:
    return {
        "filename": filename,
        # ==== Basic statistics ====
        "total_lines": 0,  
        "total_paragraphs": 0,  
        "total_sentences": 0,  
        "total_words": 0,  
        "total_characters_with_spaces": 0,  
        "total_characters_without_spaces": 0,  
        "avg_words_per_line": 0.0, 
        # ==== Word analysis ====
        "ten_most_common_words": {},  
        "shortest_word": "aaaaaaaaa",  
        "longest_word": "",  
        "avg_word_length": 0.0,  
        "word_length_distribution": [],
        "unique_word_count": 0,  
        "words_appearing_once": 0,  
        # ==== Sentence analysis ====
        "average_words_per_sentence": 0.0,  
        "longest_sentence": "",  
        "shortest_sentence": "aa aa aa aa aa aa aa aa aa aa aa aa aa aa aa aa aa aa",  
        "sentence_length_distribution": [],  
        # ==== Character analysis ====
        "total_letters": 0,  
        "total_digits": 0,  
        "total_spaces": 0,  
        "total_punctuation": 0,  
        "letter_frequency_distribution": {},  
        "punctuation_distribution": {},  
        "case_distribution": [0, 0],  
        "ten_most_common_letters": {}, 
        # ==== Readability scores ====
        "lix_score": 0.0,  
        "long_words": 0,  
    }


def initialize_analysis_data() -> dict[str, any]:
    return {  # Initialize the data structures used during analysis
        "all_words": {},  # used for 10 most common words
        "word_lengths": [0 for _ in range(45)],
        "sentence_lengths": [],
        "current_word": "",
        "current_sentence": "",
        "unique_words": set(),
        "long_words": 0,  # words with more than 6 characters (for LIX score)
    }


def process_line(line: str, statistics: dict, analysis_data: dict) -> None:
    statistics["total_lines"] += 1
    for char in line:
        process_character(char, statistics, analysis_data)


def process_character(char: str, statistics: dict, analysis_data: dict) -> None:
    statistics["total_characters_with_spaces"] += 1
    analysis_data["current_sentence"] += char

    # Check if we are at the end of a sentence
    if char in SENTENCE_ENDERS and analysis_data["current_word"].lower() not in SENTENCE_EXCEPTIONS:
        statistics["sentence_length_distribution"] = add_sentence_length_distribution(statistics["sentence_length_distribution"], analysis_data["current_sentence"])

        statistics["longest_sentence"] = (analysis_data["current_sentence"].strip() if length_in_words(analysis_data["current_sentence"]) > length_in_words(statistics["longest_sentence"]) else statistics["longest_sentence"])
        statistics["shortest_sentence"] = (analysis_data["current_sentence"].strip() if length_in_words(analysis_data["current_sentence"]) < length_in_words(statistics["shortest_sentence"]) and (length_in_words(analysis_data['current_sentence']) > 2) else statistics["shortest_sentence"])

        statistics["total_sentences"] += 1

        analysis_data["current_sentence"] = ""

    if char.isdigit():
        statistics['total_digits'] += 1

    if char.isspace():
        statistics['total_spaces'] += 1

    if char in PUNCTUATION:
        statistics['total_punctuation'] += 1
        add_to_punctuation_distribution(char, statistics)

    # Check if we are at the end of a word
    if char.isalpha():
        analysis_data["current_word"] += char.lower()

        add_to_case_distribution(char, statistics)

        add_to_letter_frequency_distribution(char, statistics)

        statistics['total_letters'] += 1
    else:
        finalize_current_word(statistics, analysis_data)

    # TODO: handle doesn't and cases like this

def add_to_case_distribution(char: str, statistics: dict):
    if char.isupper():
        statistics['case_distribution'][1] += 1
    else:
        statistics["case_distribution"][0] += 1


def add_to_letter_frequency_distribution(char: str, statistics: dict) -> None:
    if char.lower() in statistics["letter_frequency_distribution"]:
        statistics["letter_frequency_distribution"][char.lower()] += 1
    else:
        statistics["letter_frequency_distribution"][char.lower()] = 1


def add_to_punctuation_distribution(char: str, statistics: dict) -> None:
    if char.lower() in statistics["punctuation_distribution"]:
        statistics["punctuation_distribution"][char.lower()] += 1
    else:
        statistics["punctuation_distribution"][char.lower()] = 1


def finalize_current_word(statistics: dict, analysis_data: dict) -> None:
    current_word = analysis_data["current_word"]

    if current_word:
        statistics["total_words"] += 1
        analysis_data["unique_words"].add(current_word)  # unique_words is a set

        if current_word in analysis_data["all_words"]:  # all_words is a dict
            analysis_data["all_words"][current_word] += 1
        else:
            analysis_data["all_words"][current_word] = 1

        statistics["total_characters_without_spaces"] += len(current_word)
        analysis_data["word_lengths"][len(current_word) - 1] += 1

        if len(current_word) > 6:
            analysis_data["long_words"] += 1

        if len(statistics["shortest_word"]) > len(current_word):
            statistics["shortest_word"] = current_word

        if len(statistics["longest_word"]) < len(current_word):
            statistics["longest_word"] = current_word

        # reset the current word
        analysis_data["current_word"] = ""


def finalize_remaining_data(statistics: dict, analysis_data: dict) -> None:
    finalize_current_word(statistics, analysis_data)

    # Finalize the current sentence if it exists, it might not be ending with punctuation
    if analysis_data["current_sentence"]:
        statistics["sentence_length_distribution"] = add_sentence_length_distribution(statistics["sentence_length_distribution"], analysis_data["current_sentence"])

        statistics["total_sentences"] += 1


def calculate_final_statistics(statistics: dict, analysis_data: dict) -> None:
    if statistics["total_lines"] > 0:
        statistics["avg_words_per_line"] = (statistics["total_words"] / statistics["total_lines"])

    if statistics["total_words"] > 0:
        statistics["avg_word_length"] = statistics["total_characters_without_spaces"] / statistics["total_words"]

    statistics["ten_most_common_words"] = most_common_words(analysis_data["all_words"])
    statistics['ten_most_common_letters'] = most_common_words(statistics['letter_frequency_distribution'])

    statistics["word_length_distribution"] = remove_trailing_zeros(
        analysis_data["word_lengths"]
    )

    statistics["unique_word_count"] = len(analysis_data["unique_words"])

    statistics["words_appearing_once"] = word_appearing_only_once(analysis_data["all_words"])

    statistics["average_words_per_sentence"] = (statistics["total_words"] / statistics["total_sentences"])

    statistics["long_words"] = analysis_data["long_words"]
    statistics["lix_score"] = calculate_lix_score(statistics)


def most_common_words(all_words: dict) -> dict:
    top_words = {}
    for _ in range(TOP_WORDS_COUNT):
        if not all_words:
            break
        max_val = max(all_words, key=all_words.get)
        top_words[max_val] = all_words[max_val]
        all_words.pop(max_val)

    return top_words


def list_true_length(word_len_lst: list) -> int:
    # Returns the length of the list, only counting elements different from 0
    true_length = 0
    for element in word_len_lst:
        if element != 0:
            true_length += 1

    return true_length


def remove_trailing_zeros(word_len_lst: list) -> list:
    for index, word_len in enumerate(word_len_lst[::-1]):
        if word_len != 0:
            return word_len_lst[0:index]

    return word_len_lst


def word_appearing_only_once(all_words: dict) -> int:
    words_only_once = 0

    for word in all_words:
        if all_words[word] == 1:
            words_only_once += 1

    return words_only_once


def length_in_words(sentence: str) -> int:
    cleaned_sentence = ""
    for char in sentence:
        if char.isalpha() or char.isspace():
            cleaned_sentence += char
        else:
            cleaned_sentence += " "

    words = cleaned_sentence.split()
    return len(words)


def add_sentence_length_distribution(sentence_length_distribution: list, current_sentence: str) -> list:
    # Checks if the sentence is not just a single dot.
    if length_in_words(current_sentence) > 0:
        if len(sentence_length_distribution) < length_in_words(current_sentence):
            # The list is extended by as many spaces as the difference between the current sentence and the distribution list
            difference = length_in_words(current_sentence) - len(sentence_length_distribution)
            sentence_length_distribution.extend([0 for _ in range(difference)])
            sentence_length_distribution[length_in_words(current_sentence) - 1] = 1
        else:
            sentence_length_distribution[length_in_words(current_sentence) - 1] += 1

    return sentence_length_distribution


def calculate_lix_score(statistics: dict) -> float:
    # LIX = (words / sentences) + (long_words × 100 / words)
    # where long_words are words with more than 6 characters
    if statistics["total_sentences"] == 0 or statistics["total_words"] == 0:
        return 0.0

    words_per_sentence = statistics["total_words"] / statistics["total_sentences"]
    long_words_percentage = (statistics["long_words"] * 100) / statistics["total_words"]

    lix_score = words_per_sentence + long_words_percentage

    return lix_score
