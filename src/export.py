from datetime import datetime


PATH = '../exports/'
# Color codes
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"  # Reset to default color


def export_to_txt(statistics: dict):
    export_name = statistics['filename'] + '_results.txt'

    try:
        with open(PATH + export_name, 'w') as file:
            file.write('============================================================\n')
            file.write('\tTEXT ANALYSIS RESULTS\n')
            file.write('============================================================\n')

            file.write(f'File analysed: {statistics['filename']}\n')
            file.write(f'Analysis date: {datetime.now().strftime('%Y-%m-%d')}\n\n')

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

            file.write('TOP 10 MOST COMMON WORDS\n')
            file.write('------------------------------\n')
            for i, word in enumerate(statistics["ten_most_common_words"]):
                file.write(f"{i + 1:<3}- {word:<8}{statistics['ten_most_common_words'][word]:<8} times ({statistics['ten_most_common_words'][word] / statistics['total_words'] * 100:.2f} %)\n")

            file.write('\nWORD STATISTICS\n')
            file.write('--------------------\n')
            file.write(f'Shortest word: {statistics["shortest_word"]}\n')
            file.write(f'Longest word: {statistics["longest_word"]}\n')
            file.write(f'Words appearing only once: {statistics["words_appearing_once"]}\n\n')

            file.write('SENTENCE STATISTICS\n')
            file.write('-------------------------\n')
            file.write(f'Total sentences: {statistics["total_sentences"]}\n')
            file.write(f'Shortest sentence: {len(statistics["shortest_sentence"])}\n')
            file.write(f'Longest sentence: {len(statistics["longest_sentence"])}\n')
            file.write(f'Shortest sentence text: {statistics["shortest_sentence"]}\n')
            file.write(f'Longest sentence text: {statistics["longest_sentence"]}\n\n')

            file.write('CHARACTER STATISTICS\n')
            file.write('-------------------------\n')
            file.write(f'Letters: {statistics["total_letters"]}\n')
            file.write(f'Digits: {statistics["total_digits"]}\n')
            file.write(f'Spaces: {statistics["total_spaces"]}\n')
            file.write(f'Punctuation: {statistics["total_punctuation"]}\n\n')

            file.write('TOP 10 MOST COMMON LETTERS\n')
            file.write('------------------------------\n')
            for i, letter in enumerate(statistics["ten_most_common_letters"]):
                file.write(f"{i + 1:<3}- {letter:<8}{statistics['ten_most_common_letters'][letter]:<8} times ({statistics['ten_most_common_letters'][letter] / statistics['total_characters_with_spaces'] * 100:.2f} %)\n")

            file.write('\n============================================================\n')
            file.write('End of Analysis Report\n')
            file.write('============================================================\n')

            file.write(f'\n')

            print(f'{GREEN}Results exported to {PATH}{export_name}')
            print(f'Results saved in simple text format - easy to read and understand!{RESET}')
    except IOError:
        print(f'{RED}There was an error writing to file!{RESET}')
    return None