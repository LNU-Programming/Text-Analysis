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
    print(f"Average word length: {statistics['avg_words_per_line']:.2f}")

    print("\nGenerating basic statistics visualization...")
    # TODO: generate Matplotlib visualization
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
    print(f"Shortest sentence: {len(statistics['shortest_sentence'])}")
    print(f"Longest sentence: {len(statistics['longest_sentence'])}")

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
    # TODO: my brain fuzzy rn, I don't know how to do percentages LOL rip TuT
    print(f'\tLetters: {statistics['total_letters']}, ({statistics['total_characters_with_spaces'] / statistics['total_letters']}%)')
    print(f'\tDigits: {statistics["total_digits"]}, ({statistics["total_characters_with_spaces"] / statistics["total_digits"]}%)')
    print(f'\tSpaces: {statistics["total_spaces"]}, ({statistics["total_characters_with_spaces"] / statistics["total_spaces"]}%)')
    print(f'\tPunctuation: {statistics["total_punctuation"]}, ({statistics["total_characters_with_spaces"] / statistics["total_punctuation"]}%)')

    print('\nMost common letters:')
    for i, key in enumerate(statistics['letter_frequency_distribution']):
        # TODO: Again, I can't count. Add the percentage in here pleaseeee
        print(f'{i + 1:<3} - "{key}": {statistics['letter_frequency_distribution'][key]} (0%)')

    print('Generating character analysis visualisation...')
    # TODO: generate Matplotlib visualization
    print('Press ENTER to continue...')

    return None