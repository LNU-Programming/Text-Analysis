import analyse
import graph

def basic_statistics(statistics: dict) -> None:
    print(f'--- Basic Statistics for "{statistics["filename"]}" ---')
    print(f"Lines: {statistics['total_lines']}")
    print(f"Paragraphs: {statistics['total_paragraphs']}")
    print(f"Sentences: {statistics['total_sentences']}")
    print(f"Words: {statistics['total_words']}")
    print(f"Characters (with spaces): {statistics['total_characters_with_spaces']}")
    print(
        f"Characters (without spaces): {statistics['total_characters_without_spaces']}"
    )
    print(f"Average words per line: {statistics['avg_words_per_line']:.2f}")
    print(f"Average words per sentence: {statistics['average_words_per_sentence']:.2f}")
    print(f"Average word length: {statistics['avg_word_length']:.2f}")

    print("\nGenerating basic statistics visualization...")
    # TODO: generate Matplotlib visualization

    graph.text_composition_graph(statistics)

    print("Press ENTER to continue...")
    return None


def word_analysis(statistics) -> None:
    print(f'--- Word Analysis for "{statistics["filename"]}" ---')
    print("Top 10 most common words:")
    for i, word in enumerate(statistics["ten_most_common_words"]):
        print(
            f"{i + 1:<3}- {word:<8}{statistics['ten_most_common_words'][word]:<8} times ({statistics['ten_most_common_words'][word] / statistics['total_words'] * 100:.2f} %)"
        )

    print("\nWord length statistics:")
    print(
        f"\tShortest word: {statistics['shortest_word']}, {len(statistics['shortest_word'])} characters"
    )
    print(
        f"\tLongest word: {statistics['longest_word']}, {len(statistics['longest_word'])} characters"
    )
    print(f"\tAverage word length: {statistics['avg_word_length']:.2f} characters")
    print(f"Unique word count: {statistics['unique_word_count']}")
    print(f"Words appearing only once: {statistics['words_appearing_once']}")

    print("\nGenerating word analysis visualization...")
    # TODO: generate Matplotlib visualization
    print("Press ENTER to continue...")
    return None


def sentence_analysis(statistics) -> None:
    print(f'\n--- Sentence Analysis for "{statistics["filename"]}" ---')
    print(f"Total sentences: {statistics['total_sentences']}")
    print(f"Average words per sentence: {statistics['average_words_per_sentence']:.2f}")
    print(f"Shortest sentence: {analyse.length_in_words(statistics['shortest_sentence'])}")
    print(f"Longest sentence: {analyse.length_in_words(statistics['longest_sentence'])}")

    print(f"Shortest sentence text: {statistics['shortest_sentence']}")
    print(f"Longest sentence text: {statistics['longest_sentence']}")

    print("\nSentence length distribution:")
    for i, element in enumerate(statistics["sentence_length_distribution"]):
        print(
            f"{i + 1:<3} words: {element:<8} sentences ({element / statistics['total_sentences'] * 100:.2f} %)"
        )

    print("Generating sentence analysis visualisation...")

    print("Press Enter to continue...")

    return None

def character_analysis(statistics) -> None:
    print(f'\n--- Character Analysis for "{statistics["filename"]}" ---')
    print('Character type distribution:')

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

    print('Generating character analysis visualisation...')
    # TODO: generate Matplotlib visualization
    print('Press ENTER to continue...')

    return None
