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