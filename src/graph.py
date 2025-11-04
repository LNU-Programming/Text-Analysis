"""
Graph visualization module for text analysis statistics.

This module provides functions to create various visualizations of text statistics
using matplotlib, including pie charts, bar charts, and distribution graphs for
character types, word frequencies, sentence lengths, and other text metrics.
"""
import matplotlib.pyplot as plt


def character_type_distribution(stats: dict) -> None:
    """
    Display a pie chart showing the distribution of character types in the text.

    Args:
        stats (dict): A dictionary containing text statistics
    Returns:
        None: Displays a matplotlib pie chart window.
    """
    labels = ['Letters', 'Digits', 'Spaces', 'Punctuation']
    values = [stats['total_letters'], stats['total_digits'],
              stats['total_spaces'], stats['total_punctuation']]

    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
    plt.pie(values, labels=labels, colors=colors, autopct='%1.1f%%')
    plt.title('Character Type Distribution')
    plt.show()


def text_composition(stats: dict) -> None:
    """
    Display a bar chart showing the composition of the text by structural elements.

    Args:
        stats (dict): A dictionary containing text statistics
    Returns:
        None: Displays a matplotlib bar chart window.
    """
    categories = ['Lines', 'Paragraphs', 'Sentences', 'Words']
    values = [stats['total_lines'], stats['total_paragraphs'],
              stats['total_sentences'], stats['total_words']]

    plt.bar(categories, values, color='#5C7CFA')
    plt.title('Text Composition')
    plt.show()


def most_common_words_graph(stats: dict) -> None:
    """
    Display a bar chart of the 10 most frequently occurring words in the text.

    Args:
        stats (dict): A dictionary containing text statistics
    Returns:
        None: Displays a matplotlib bar chart window.
    """
    words = list(stats['ten_most_common_words'].keys())
    counts = list(stats['ten_most_common_words'].values())

    plt.bar(words, counts, color='#20C997')
    plt.title('10 Most Common Words')
    plt.show()


def word_length_distribution_graph(stats: dict) -> None:
    """
    Display a bar chart showing the distribution of word lengths in the text.

    Args:
        stats (dict): A dictionary containing text statistics
    Returns:
        None: Displays a matplotlib bar chart window.
    """
    lengths = list(range(1, len(stats['word_length_distribution']) + 1))
    counts = stats['word_length_distribution']

    plt.bar(lengths, counts, color='#FF8787')
    plt.title('Word Length Distribution')
    plt.show()


def sentence_length_distribution_graph(stats: dict) -> None:
    """
    Display a bar chart showing the distribution of sentence lengths in the text.

    Args:
        stats (dict): A dictionary containing text statistics
    Returns:
        None: Displays a matplotlib bar chart window.
    """
    lengths = list(range(1, len(stats['sentence_length_distribution']) + 1))
    counts = stats['sentence_length_distribution']

    plt.bar(lengths, counts, color='#AE3EC9')
    plt.title('Sentence Length Distribution')
    plt.show()


def get_count(pair: dict) -> None:
    """
    Helper function to extract the count value from a (length, count) tuple.

    Args:
        pair (tuple): A tuple containing (length, count) where count is at index 1
    Returns:
        int: The count value (second element) from the tuple
    """
    return pair[1]

def most_common_sentence_length(stats):
    """
    Display a bar chart of the 8 most common sentence lengths in the text.

    This function analyzes the sentence length distribution, identifies the 8 most
    frequently occurring sentence lengths, and displays them as a bar chart sorted
    by frequency.

    Args:
        stats (dict): A dictionary containing text statistics with keys
    Returns:
        None: Displays a matplotlib bar chart window.
    """
    distribution = stats['sentence_length_distribution']

    # Create pairs of (length, count) and sort by count descending
    pairs = [(i + 1, count) for i, count in enumerate(distribution)]

    pairs.sort(key=get_count, reverse=True)

    # Take top 8
    top_8 = pairs[:8]

    lengths = [pair[0] for pair in top_8]
    counts = [pair[1] for pair in top_8]

    plt.bar(lengths, counts, color='#FAB005')
    plt.title('8 Most Common Sentence Lengths')
    plt.show()


def ten_most_common_letters_graph(stats):
    """
    Display a bar chart of the 10 most frequently occurring letters in the text.

    Args:
        stats (dict): A dictionary containing text statistics with keys
    Returns:
        None: Displays a matplotlib bar chart window.
    """
    letters = list(stats['ten_most_common_letters'].keys())
    counts = list(stats['ten_most_common_letters'].values())

    plt.bar(letters, counts, color='#51CF66')
    plt.title('10 Most Common Letters')
    plt.show()
