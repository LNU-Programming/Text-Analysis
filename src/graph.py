import matplotlib.pyplot as plt


def character_type_distribution(stats):
    labels = ['Letters', 'Digits', 'Spaces', 'Punctuation']
    values = [stats['total_letters'], stats['total_digits'],
              stats['total_spaces'], stats['total_punctuation']]

    plt.pie(values, labels=labels)
    plt.show()


def text_composition(stats):
    categories = ['Lines', 'Paragraphs', 'Sentences', 'Words']
    values = [stats['total_lines'], stats['total_paragraphs'],
              stats['total_sentences'], stats['total_words']]

    plt.bar(categories, values)
    plt.show()


def most_common_words_graph(stats):
    words = list(stats['ten_most_common_words'].keys())
    counts = list(stats['ten_most_common_words'].values())

    plt.bar(words, counts)
    plt.show()


def word_length_distribution_graph(stats):
    lengths = list(range(1, len(stats['word_length_distribution']) + 1))
    counts = stats['word_length_distribution']

    plt.bar(lengths, counts)
    plt.show()


def sentence_length_distribution_graph(stats):
    lengths = list(range(1, len(stats['sentence_length_distribution']) + 1))
    counts = stats['sentence_length_distribution']

    plt.bar(lengths, counts)
    plt.show()


def most_common_sentence_length(stats):
    distribution = stats['sentence_length_distribution']

    # Create pairs of (length, count) and sort by count descending
    pairs = [(i + 1, count) for i, count in enumerate(distribution)]
    pairs.sort(key=lambda x: x[1], reverse=True)

    # Take top 8
    top_8 = pairs[:8]

    lengths = [pair[0] for pair in top_8]
    counts = [pair[1] for pair in top_8]

    plt.bar(lengths, counts)
    plt.show()

def ten_most_common_letters_graph(stats):
    letters = list(stats['ten_most_common_letters'].keys())
    counts = list(stats['ten_most_common_letters'].values())

    plt.bar(letters, counts)
    plt.show()