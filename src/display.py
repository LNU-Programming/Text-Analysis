import analyse
import graph

BOLD = '\033[1m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
RESET = '\033[0m'

def basic_statistics(statistics: dict) -> None:
    print(f'{BOLD}--- Basic Statistics for "{statistics["filename"]}" ---{RESET}')
    print(f"\nLines: {statistics['total_lines']}")
    print(f"Paragraphs: {statistics['total_paragraphs']}")
    print(f"Sentences: {statistics['total_sentences']}")
    print(f"Words: {statistics['total_words']}")
    print(f"Characters (with spaces): {statistics['total_characters_with_spaces']}")
    print(f"Characters (without spaces): {statistics['total_characters_without_spaces']}")
    print(f"Average words per line: {statistics['avg_words_per_line']:.2f}")
    print(f"Average words per sentence: {statistics['average_words_per_sentence']:.2f}")
    print(f"Average word length: {statistics['avg_word_length']:.2f}")

    print(f"\n{ITALIC}Generating basic statistics visualization...{RESET}")

    graph.text_composition(statistics)
    graph.character_type_distribution(statistics)

    return None


def word_analysis(statistics) -> None:
    print(f'{BOLD}--- Word Analysis for "{statistics["filename"]}" ---{RESET}')
    print("\nTop 10 most common words:")
    for i, word in enumerate(statistics["ten_most_common_words"]):
        print(f"{i + 1:<3}- {word:<8}{statistics['ten_most_common_words'][word]:<8} times ({statistics['ten_most_common_words'][word] / statistics['total_words'] * 100:.2f} %)")

    print("\nWord length statistics:")
    print(f"\tShortest word: {ITALIC}{statistics['shortest_word']}{RESET}, {len(statistics['shortest_word'])} characters")
    print(f"\tLongest word: {ITALIC}{statistics['longest_word']}{RESET}, {len(statistics['longest_word'])} characters")
    print(f"\tAverage word length: {statistics['avg_word_length']:.2f} characters")
    print(f"Unique word count: {statistics['unique_word_count']}")
    print(f"Words appearing only once: {statistics['words_appearing_once']}")

    print(F"\n{ITALIC}Generating word analysis visualization...{RESET}")

    graph.most_common_words_graph(statistics)
    graph.word_length_distribution_graph(statistics)

    return None


def sentence_analysis(statistics) -> None:
    print(f'\n{BOLD}--- Sentence Analysis for "{statistics["filename"]}" ---{RESET}')

    lix_score = statistics["lix_score"]
    if lix_score < 25:
        difficulty = "Very Easy (children's books)"
    elif lix_score < 35:
        difficulty = "Easy (fiction, popular magazines)"
    elif lix_score < 45:
        difficulty = "Medium (newspaper text)"
    elif lix_score < 55:
        difficulty = "Difficult (technical/professional text)"
    else:
        difficulty = "Very Difficult (academic/legal text)"

    print(f'\nLIX Readability Score: {lix_score:.2f} - {difficulty}')
    print(f'Long words (>6 characters): {statistics["long_words"]} ({statistics["long_words"] / statistics["total_words"] * 100:.2f}%)')


    print(f"\nTotal sentences: {statistics['total_sentences']}")
    print(f"Average words per sentence: {statistics['average_words_per_sentence']:.2f}")
    print(f"Shortest sentence: {analyse.length_in_words(statistics['shortest_sentence'])}")
    print(f"Longest sentence: {analyse.length_in_words(statistics['longest_sentence'])}")

    print(f"\nShortest sentence text: {ITALIC}{statistics['shortest_sentence']}{RESET}")
    print(f"\nLongest sentence text:\n{ITALIC}{statistics['longest_sentence']}{RESET}")

    print("\nSentence length distribution:")
    copy_of_distribution = statistics["sentence_length_distribution"]
    for i in range(5):
        print(f'{i + 1:<3} words: {max(copy_of_distribution):<4} sentences ({max(copy_of_distribution) / statistics['total_sentences'] * 100:.2f} %)')
        copy_of_distribution.remove(max(copy_of_distribution))

    print(F"\n{ITALIC}Generating sentence analysis visualisation...{RESET}")
    graph.sentence_length_distribution_graph(statistics)
    graph.most_common_sentence_length(statistics)

    return None

def character_analysis(statistics) -> None:
    print(f'\n{BOLD}--- Character Analysis for "{statistics["filename"]}" ---{RESET}')
    print('\nCharacter type distribution:')

    if statistics['total_characters_with_spaces'] > 0:
        percentage_letters = (statistics['total_letters'] / statistics['total_characters_with_spaces']) * 100
        percentage_digits = (statistics['total_digits'] / statistics['total_characters_with_spaces']) * 100
        percentage_spaces = (statistics['total_spaces'] / statistics['total_characters_with_spaces']) * 100
        percentage_punctuation = (statistics['total_punctuation'] / statistics['total_characters_with_spaces']) * 100
    else:
        percentage_letters = 0
        percentage_digits = 0
        percentage_spaces = 0
        percentage_punctuation = 0

    print(f'\tLetters: {statistics["total_letters"]}, {percentage_letters:.2f}%')
    print(f'\tDigits: {statistics["total_digits"]}, {percentage_digits:.2f}%')
    print(f'\tSpaces: {statistics["total_spaces"]}, {percentage_spaces:.2f}%')
    print(f'\tPunctuation: {statistics["total_punctuation"]}, {percentage_punctuation:.2f}%')

    # TODO: character ordering
    print('\nLetters distribution:')
    for i, key in enumerate(statistics['letter_frequency_distribution']):
        percentage = (statistics['letter_frequency_distribution'][key] / statistics['total_characters_with_spaces']) * 100
        print(f'{i + 1:<2} - "{key}" : {statistics['letter_frequency_distribution'][key]:<8} ({percentage:.2f}%)')

    print('\nPunctuation distribution:')
    for i, key in enumerate(statistics['punctuation_distribution']):
        percentage = (statistics['punctuation_distribution'][key] / statistics[
            'total_characters_with_spaces']) * 100
        print(f'{i + 1:<2} - "{key}" : {statistics['punctuation_distribution'][key]:<8} ({percentage:.2f}%)')

    print('\nLower/upper case distribution:')
    print(f'\tLower characters: {statistics['case_distribution'][0]}')
    print(f'\tUpper characters: {statistics['case_distribution'][1]}')

    print(f'\n{ITALIC}Generating character analysis visualisation...{RESET}')
    graph.ten_most_common_letters_graph(statistics)
    graph.character_type_distribution(statistics)

    return None
