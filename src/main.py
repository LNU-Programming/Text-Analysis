import load
import time
import display
import export

"""
ANSI color codes are special character sequences that add color and formatting
to terminal text output.

Structure:
    '\\033[<code>m'

    - \\033 = Escape character for ANSI sequences
    - [     = Starts the sequence
    - <code>= Number defining the color/style
    - m     = Ends the sequence
"""
BOLD = '\033[1m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
RESET = '\033[0m'  # Reset to default color


def main():
    flag = True
    statistics = {"filename": ""}

    while flag:
        print("\n=====================================")
        print(f"\t\t{BOLD}TEXT ANALYZER{RESET}")
        print("=====================================")
        print("\t 1) Load a basic text file")
        print("\t 2) Display basic statistics")
        print("\t 3) Show word frequency analysis")
        print("\t 4) Display sentence analysis")
        print("\t 5) Display character analysis")
        print("\t 6) Export results")
        print("\t 0) Exit program")
        print("=====================================")
        print(f"\t{ITALIC}{CYAN}{('Current file: ' + statistics['filename']) if statistics['filename'] != '' else 'No file loaded'}{RESET}")

        choice = input("\n\tInsert your choice (0 - 6): ")
        match choice:
            case "1":
                print()
                statistics = load.load_file()
            case "2":
                print()
                if statistics['filename'] == '':
                    print(f'{RED}You need to load a file first!{RESET}')
                    continue
                display.basic_statistics(statistics)
            case "3":
                print()
                if statistics['filename'] == '':
                    print(f'{RED}You need to load a file first!{RESET}')
                    continue
                display.word_analysis(statistics)
            case "4":
                print()
                if statistics['filename'] == '':
                    print(f'{RED}You need to load a file first!{RESET}')
                    continue
                display.sentence_analysis(statistics)
            case "5":
                print()
                if statistics['filename'] == '':
                    print(f'{RED}You need to load a file first!{RESET}')
                    continue
                display.character_analysis(statistics)
            case "6":
                print()
                if statistics['filename'] == '':
                    print(f'{RED}You need to load a file first!{RESET}')
                    continue
                export.export_to_txt(statistics)
            case "0":
                print("Exiting the program...")
                flag = False
            case _:
                print(f"\n\t{RED}Invalid choice! Please select a number between 0 and 6.{RESET}")
                time.sleep(3)


main()
