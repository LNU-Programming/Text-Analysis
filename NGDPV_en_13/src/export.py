"""Export module for text analysis results.
This module provides functionality to export text analysis statistics to a formatted
text file. It generates a comprehensive report including basic statistics, word analysis,
sentence analysis, and character statistics.
"""
import os
from datetime import datetime
from src import analyse

# Get the absolute path to the exports directory
current_dir = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(current_dir)  # Go up one level from src/ to project root
PATH = os.path.join(PROJECT_ROOT, 'exports')

# Color codes
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"  # Reset to default color

def export_to_txt(statistics: dict):
    """Export text analysis statistics to a formatted text file.
    Creates a comprehensive analysis report file with formatted sections for basic
    statistics, word statistics, sentence statistics, and character statistics.
    The file is saved in the exports directory with a filename based on the
    analyzed text's filename.
    Args:
        statistics (dict): A dictionary containing all analysis results with keys including:
    Returns:
        None
    """
    export_name = statistics['filename'] + '_results.txt'
    try:
        # Use os.path.join for proper path concatenation
        export_path = os.path.join(PATH, export_name)
        
        with open(export_path, 'w', encoding='utf-8') as file:
            file.write('============================================================\n')
            file.write('\tTEXT ANALYSIS RESULTS\n')
            file.write('============================================================\n')
            file.write(f'File analysed: {statistics['filename']}\n')
            file.write(f'Analysis date: {datetime.now().strftime('%Y-%m-%d')}\n\n')
            write_basic_statistics(file, statistics)
            write_word_statistics(file, statistics)
            write_sentence_statistics(file, statistics)
            write_character_statistics(file, statistics)
            file.write('\n============================================================\n')
            file.write('End of Analysis Report\n')
            file.write('============================================================\n')
            file.write(f'\n')
            print(f'{GREEN}Results exported to {export_path}')
            print(f'Results saved in simple text format - easy to read and understand!{RESET}')
    except IOError:
        print(f'{RED}There was an error writing to file!{RESET}')
    return None


def write_character_statistics(file, statistics):
    """Write character statistics section to the export file.

    Outputs detailed character analysis including counts of letters, digits, spaces,
    and punctuation marks. Also includes the top 10 most common letters with their
    frequencies and percentages.

    Args:
        file: File object opened in write mode
        statistics (dict): Dictionary containing character statistics with keys:
    Returns:
        None
    """
    file.write('CHARACTER STATISTICS\n')
    file.write('-------------------------\n')
    file.write(f'Letters: {statistics["total_letters"]}\n')
    file.write(f'Digits: {statistics["total_digits"]}\n')
    file.write(f'Spaces: {statistics["total_spaces"]}\n')
    file.write(f'Punctuation: {statistics["total_punctuation"]}\n\n')
    file.write('TOP 10 MOST COMMON LETTERS\n')
    file.write('------------------------------\n')
    for i, letter in enumerate(statistics["ten_most_common_letters"]):
        file.write(
            f"{i + 1:<3}- {letter:<8}{statistics['ten_most_common_letters'][letter]:<8} times ({statistics['ten_most_common_letters'][letter] / statistics['total_characters_with_spaces'] * 100:.2f} %)\n")


def write_sentence_statistics(file, statistics):
    """Write sentence statistics section to the export file.

    Outputs sentence analysis including total sentence count, shortest and longest
    sentence lengths in words, and the full text of both the shortest and longest
    sentences.

    Args:
        file: File object opened in write mode
        statistics (dict): Dictionary containing sentence statistics with keys:
    Returns:
        None
    """
    file.write('\nSENTENCE STATISTICS\n')
    file.write('-------------------------\n')
    file.write(f'Total sentences: {statistics["total_sentences"]}\n')
    file.write(f'Shortest sentence: {analyse.length_in_words(statistics["shortest_sentence"])}\n')
    file.write(f'Longest sentence: {analyse.length_in_words(statistics["longest_sentence"])}\n')
    file.write(f'\nShortest sentence text:\n {statistics["shortest_sentence"]}\n')
    file.write(f'\nLongest sentence text:\n {statistics["longest_sentence"]}\n\n')


def write_word_statistics(file, statistics):
    """Write word statistics section to the export file.

    Outputs word analysis including shortest and longest words, words appearing only
    once, and the top 10 most common words with their frequencies and percentages.

    Args:
        file: File object opened in write mode
        statistics (dict): Dictionary containing word statistics with keys:
    Returns:
        None
    """
    file.write('\nWORD STATISTICS\n')
    file.write('--------------------\n')
    file.write(f'Shortest word: {statistics["shortest_word"]}\n')
    file.write(f'Longest word: {statistics["longest_word"]}\n')
    file.write(f'Words appearing only once: {statistics["words_appearing_once"]}\n\n')
    file.write('TOP 10 MOST COMMON WORDS\n')
    file.write('------------------------------\n')
    for i, word in enumerate(statistics["ten_most_common_words"]):
        file.write(
            f"{i + 1:<3}- {word:<8}{statistics['ten_most_common_words'][word]:<8} times ({statistics['ten_most_common_words'][word] / statistics['total_words'] * 100:.2f} %)\n")


def write_basic_statistics(file, statistics):
    """Write basic statistics section to the export file.

    Outputs fundamental text metrics including counts of lines, paragraphs, sentences,
    words, and characters, as well as calculated averages for words per line, word
    length, and words per sentence.

    Args:
        file: File object opened in write mode
        statistics (dict): Dictionary containing basic statistics with keys:
    Returns:
        None
    """
    file.write('BASIC STATISTICS\n')
    file.write('--------------------\n')
    file.write(f'Lines: {statistics['total_lines']}\n')
    file.write(f'Paragraphs: {statistics['total_paragraphs']}\n')
    file.write(f'Sentences: {statistics['total_sentences']}\n')
    file.write(f'Words: {statistics['total_words']}\n')
    file.write(f'Unique words: {statistics['unique_word_count']}\n')
    file.write(f'Characters (with spaces): {statistics['total_characters_with_spaces']}\n')
    file.write(f'Characters (without spaces): {statistics['total_characters_without_spaces']}\n')
    file.write(f'Average words per line: {statistics['avg_words_per_line']:.2f}\n')
    file.write(f'Average word length: {statistics['avg_word_length']:.2f}\n')
    file.write(f'Average words per sentence: {statistics['average_words_per_sentence']:.2f}\n\n')
