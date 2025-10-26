def analyse_file(path: str, filename: str) -> dict[str, any]:
    statistics = initialize_statistics(filename)
    analysis_data = initialize_analysis_data()

    try:
        with open(f"{path}{filename}", "r") as file:
            for line in file:
                process_line(line, statistics, analysis_data)

        # Finalize any remaining words or sentences
        finalize_remaining_data(statistics, analysis_data)
        calculate_final_statistics(statistics, analysis_data)

    except FileNotFoundError:
        print("File not found.")

    print(f"Analysis complete! Processed {statistics['total_lines']} lines.")
    print(f'Successfully loaded and analyzed "{statistics["filename"]}"')
    return statistics


def initialize_statistics(filename: str) -> dict[str, any]:
    """Initialize the statistics dictionary with default values."""
    return {
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


def initialize_analysis_data() -> dict[str, any]:
    """Initialize data structures used during analysis."""
    return {
        "all_words": {},
        "word_lengths": [],
        "sentence_lengths": [],
        "current_word": "",
        "current_sentence": "",
    }


def process_line(line: str, statistics: dict, analysis_data: dict) -> None:
    """Process a single line of text and update statistics."""
    statistics["total_lines"] += 1

    for char in line:
        process_character(char, statistics, analysis_data)


def process_character(char: str, statistics: dict, analysis_data: dict) -> None:
    """Process a single character and update analysis state."""
    statistics["total_characters_with_spaces"] += 1

    # Update current sentence
    analysis_data["current_sentence"] += char

    # Check for sentence end
    if char in ".!?":
        analysis_data["sentence_lengths"].append(len(analysis_data["current_sentence"]))
        analysis_data["current_sentence"] = ""

    # Process word boundaries
    if char.isalpha():
        analysis_data["current_word"] += char.lower()
    else:
        finalize_current_word(statistics, analysis_data)


def finalize_current_word(statistics: dict, analysis_data: dict) -> None:
    """Finalize the current word if it exists and reset for next word."""
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
    """Finalize any remaining words or sentences at the end of the file."""
    # Finalize current word if it exists
    finalize_current_word(statistics, analysis_data)

    # Finalize current sentence if it exists (not ending with punctuation)
    if analysis_data["current_sentence"]:
        analysis_data["sentence_lengths"].append(len(analysis_data["current_sentence"]))


def calculate_final_statistics(statistics: dict, analysis_data: dict) -> None:
    """Calculate final statistics after processing all text."""
    # Calculate averages
    if statistics["total_lines"] > 0:
        statistics["avg_words_per_line"] = statistics["total_words"] / statistics["total_lines"]

    if statistics["total_words"] > 0:
        statistics["avg_char_per_word"] = (
            statistics["total_characters_without_spaces"] / statistics["total_words"]
        )

    # Calculate most common words
    statistics["ten_most_common_words"] = most_common_words(analysis_data["all_words"])


def most_common_words(all_words: dict) -> dict:
    top_ten_words = {}
    for _ in range(10):
        max_val = max(all_words, key=all_words.get)
        top_ten_words[max_val] = all_words[max_val]
        all_words.pop(max_val)

    return top_ten_words
