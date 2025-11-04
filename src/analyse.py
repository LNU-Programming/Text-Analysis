# Color codes
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"  # Reset to default color

SENTENCE_ENDERS = (".", "!", "?", ':--')
SENTENCE_EXCEPTIONS = ("dr", "mr", "st", "mrs", "ms", "inc", "ltd", "co", "corp", "llc", "plc", "u.s", "u.k", "e.u", "u.n", "ph.d", "e.g", "i.e", "etc")
TOP_WORDS_COUNT = 10
PUNCTUATION = ('!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~')


def analyse_file(path: str, filename: str) -> dict[str, any]:
    """
    Analyze a text file and compute comprehensive statistics.
    
    Args:
        path: Directory path where the file is located
        filename: Name of the file to analyze
        
    Returns:
        Dictionary containing all computed statistics
    """
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
    """
    Initialize the statistics dictionary.
    
    Args:
        filename: Name of the file being analyzed
        
    Returns:
        Dictionary with all statistic fields
    """
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
    """
    Initialize temporary data structures used during text analysis.
    
    Returns:
        Dictionary containing temporary data structures for tracking words,
        sentences, and other metrics during the analysis process
    """
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
    """
    Process a single line of text by analyzing each character.
    
    Args:
        line: Text line to process
        statistics: Dictionary to store computed statistics
        analysis_data: Dictionary with temporary analysis data
    """
    statistics["total_lines"] += 1
    for char in line:
        process_character(char, statistics, analysis_data)


def process_character(char: str, statistics: dict, analysis_data: dict) -> None:
    """
    Process a single character and update statistics accordingly.
    
    Handles character classification (letters, digits, spaces, punctuation),
    words and sentences.
    
    Args:
        char: Single character to process
        statistics: Dictionary to store computed statistics
        analysis_data: Dictionary with temporary analysis data
    """
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
    """
    Update the case distribution statistics for a character.
    
    Tracks lowercase (index 0) and uppercase (index 1) character counts.
    
    Args:
        char: Character to check (must be alphabetic)
        statistics: Dictionary to store computed statistics
    """
    if char.isupper():
        statistics['case_distribution'][1] += 1
    else:
        statistics["case_distribution"][0] += 1


def add_to_letter_frequency_distribution(char: str, statistics: dict) -> None:
    """
    Update the letter frequency distribution for a character.
    
    Args:
        char: Character to add to distribution (converted to lowercase)
        statistics: Dictionary to store computed statistics
    """
    if char.lower() in statistics["letter_frequency_distribution"]:
        statistics["letter_frequency_distribution"][char.lower()] += 1
    else:
        statistics["letter_frequency_distribution"][char.lower()] = 1


def add_to_punctuation_distribution(char: str, statistics: dict) -> None:
    """
    Update the punctuation frequency distribution.
    
    Args:
        char: Punctuation character to add to distribution
        statistics: Dictionary to store computed statistics
    """
    if char.lower() in statistics["punctuation_distribution"]:
        statistics["punctuation_distribution"][char.lower()] += 1
    else:
        statistics["punctuation_distribution"][char.lower()] = 1


def finalize_current_word(statistics: dict, analysis_data: dict) -> None:
    """
    Finalize the current word being processed and update all relevant statistics.
    
    Updates word count, unique words, word lengths, shortest/longest words,
    and resets the current word buffer.
    
    Args:
        statistics: Dictionary to store computed statistics
        analysis_data: Dictionary with temporary analysis data
    """
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
    """
    Finalize any remaining words and sentences after file processing is complete.
    
    Handles edge cases where the file doesn't end with punctuation or whitespace.
    
    Args:
        statistics: Dictionary to store computed statistics
        analysis_data: Dictionary with temporary analysis data
    """
    finalize_current_word(statistics, analysis_data)

    # Finalize the current sentence if it exists, it might not be ending with punctuation
    if analysis_data["current_sentence"]:
        statistics["sentence_length_distribution"] = add_sentence_length_distribution(statistics["sentence_length_distribution"], analysis_data["current_sentence"])

        statistics["total_sentences"] += 1


def calculate_final_statistics(statistics: dict, analysis_data: dict) -> None:
    """
    Calculate all final statistics that require complete data.
    
    Computes averages, distributions, most common words/letters, and readability scores.
    
    Args:
        statistics: Dictionary to store computed statistics
        analysis_data: Dictionary with temporary analysis data
    """
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
    """
    Extract the most common words from all words dictionary.
    
    Args:
        all_words: Dictionary mapping words to their frequencies
        
    Returns:
        Dictionary containing the top N most common words (N = TOP_WORDS_COUNT)
    """
    top_words = {}
    for _ in range(TOP_WORDS_COUNT):
        if not all_words:
            break
        max_val = max(all_words, key=all_words.get)
        top_words[max_val] = all_words[max_val]
        all_words.pop(max_val)

    return top_words


def list_true_length(word_len_lst: list) -> int:
    """
    Calculate the number of non-zero elements in a list.
    
    Args:
        word_len_lst: List of integers
        
    Returns:
        Count of elements that are not zero
    """
    # Returns the length of the list, only counting elements different from 0
    true_length = 0
    for element in word_len_lst:
        if element != 0:
            true_length += 1

    return true_length


def remove_trailing_zeros(word_len_lst: list) -> list:
    """
    Remove trailing zero elements from a list.
    
    Args:
        word_len_lst: List of integers
        
    Returns:
        List with trailing zeros removed
    """
    for index, word_len in enumerate(word_len_lst[::-1]):
        if word_len != 0:
            return word_len_lst[0:index]

    return word_len_lst


def word_appearing_only_once(all_words: dict) -> int:
    """
    Count the number of words that appear exactly once.
    
    Args:
        all_words: Dictionary mapping words to their frequencies
        
    Returns:
        Count of words with frequency equal to 1
    """
    words_only_once = 0

    for word in all_words:
        if all_words[word] == 1:
            words_only_once += 1

    return words_only_once


def length_in_words(sentence: str) -> int:
    """
    Calculate the number of words in a sentence.
    
    Cleans the sentence by keeping only alphabetic characters and spaces,
    then counts the resulting words.
    
    Args:
        sentence: Text string to analyze
        
    Returns:
        Number of words in the sentence
    """
    cleaned_sentence = ""
    for char in sentence:
        if char.isalpha() or char.isspace():
            cleaned_sentence += char
        else:
            cleaned_sentence += " "

    words = cleaned_sentence.split()
    return len(words)


def add_sentence_length_distribution(sentence_length_distribution: list, current_sentence: str) -> list:
    """
    Update the sentence length distribution.
    
    The distribution list is indexed by sentence length (in words).
    Automatically extends the list if a longer sentence is encountered.
    
    Args:
        sentence_length_distribution: List tracking sentence length frequencies
        current_sentence: The sentence to add to the distribution
        
    Returns:
        Updated sentence length distribution list
    """
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
    """
    Calculate the LIX (Läsbarhetsindex) readability score.
    
    LIX = (words / sentences) + (long_words × 100 / words)
    where long_words are words with more than 6 characters.
    
    Args:
        statistics: Dictionary containing word and sentence statistics
        
    Returns:
        LIX readability score as a float, or 0.0 if calculation is not possible
    """
    # LIX = (words / sentences) + (long_words × 100 / words)
    # where long_words are words with more than 6 characters
    if statistics["total_sentences"] == 0 or statistics["total_words"] == 0:
        return 0.0

    words_per_sentence = statistics["total_words"] / statistics["total_sentences"]
    long_words_percentage = (statistics["long_words"] * 100) / statistics["total_words"]

    lix_score = words_per_sentence + long_words_percentage

    return lix_score
