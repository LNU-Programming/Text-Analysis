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
    print(f"\tUnique word count: {statistics['unique_word_count']}")
    print(f"\tWords appearing only once: {statistics['words_appearing_once']}")

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
