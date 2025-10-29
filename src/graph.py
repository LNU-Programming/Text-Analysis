import matplotlib.pyplot as plt


def text_composition_graph(stats):
    categories = ['Letters', 'Digits', 'Spaces', 'Punctuation']
    values = [stats['total_letters'], stats['total_digits'],
              stats['total_spaces'], stats['total_punctuation']]

    plt.bar(categories, values)
    plt.show()