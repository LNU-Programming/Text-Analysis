def basic_statistics(statistics: dict) -> None:
    print(f'--- Basic Statistics for "{statistics["filename"]}" ---')
    print(f"Lines: {statistics['total_lines']}")
    print(f"Words: {statistics['total_words']}")
    print(f"Characters (with spaces): {statistics['total_characters_with_spaces']}")
    print(
        f"Characters (without spaces): {statistics['total_characters_without_spaces']}"
    )
    print(f"Average words per line: {statistics['avg_words_per_line']:.2f}")
    print(f"Average word length: {statistics['avg_char_per_word']:.2f}")

    print("\nGenerating basic statistics visualization...")
    # TODO: generate Matplotlib visualization
    print("Press ENTER to continue...")
    return None


def word_analysis(statistics) -> None:
    print(f'--- Word Analysis for "{statistics["filename"]}" ---')
    print("Top 10 most common words:")
    for i, word in enumerate(statistics["most_common_words"]):
        print(
            f"{i + 1}. {word:<6}{statistics['most_common_words'][word]} times ({statistics['most_common_words'][word] / statistics['total_words'] * 100:.2f} %)"
        )

    print("\nWord length statistics:")
    print(f"\tShortest word: 0 characters")
    print(f"\tLongest word: 0 characters")
    print(f"\tAverage word length: 0 characters")
    print(f"Words appearing only once: 0")

    print("\nGenerating word analysis visualization...")
    # TODO: generate Matplotlib visualization
    print("Press ENTER to continue...")
    return None


def sentence_analysis(statistics) -> None:
    print(f'--- Sentence Analysis for "{statistics["filename"]}" ---')
    print(f"Total sentences: 0")
    print(f"Average words per sentence: 0")
    print(f"Shortest sentence: 0")
    print(f"Longest sentence: 0")

    print(f"Shortest sentence text: a")
    print(f"Longest sentence text: a")

    return None
