import load, time

def display_basic_statistics(statistics: dict) -> None:
    print(f'--- Basic Statistics for "{statistics["filename"]}" ---')
    print(f'Lines: {statistics["total_lines"]}')
    print(f'Words: {statistics["total_words"]}')
    print(f'Characters (with spaces): {statistics["total_characters_with_spaces"]}')
    print(f'Characters (without spaces): {statistics["total_characters_without_spaces"]}')
    print(f'Average words per line: {statistics["avg_words_per_line"]}')
    print(f'Average word length: {statistics["avg_char_per_word"]}')
    return None

def main():
    flag = True
    statistics = {"filename": ""} # dictionary containing statistics for the whole book, after we selected it
    while flag:
        print("\n=====================================")
        print("\t\tTEXT ANALYZER")
        print("=====================================")
        print("\t 1) Load a basic text file")
        print("\t 2) Display basic statistics")
        print("\t 3) Show word frequency analysis")
        print("\t 4) Display sentence analysis")
        print("\t 5) Display character analysis")
        print("\t 6) Export results")
        print("\t 0) Exit program")
        print("=====================================")
        print(f"\t{ ("Current file: " + statistics["filename"]) if statistics["filename"] != "" else "No file loaded"}")

        choice = input("\n\tInsert your choice (0 - 6): ") # TODO: handle user input, also None case

        match choice:
            case "1":
                statistics = load.load_file()
            case "2":
                display_basic_statistics(statistics)
            case "3":
                print("Choice three!")
            case "4":
                print("Choice four!")
            case "5":
                print("Choice five!")
            case "6":
                print("Choice six!")
            case "0":
                print("Exiting the program...")
                flag = False
            case _:
                print("\n\tInvalid choice! Please select a number between 0 and 6.")
                time.sleep(3)
                # TODO: Add a punishment when the user enters an invalid choices multiple times. Depending how many char
                #  the user inputs.

# ----------------------------------------------------------------------------------------------------------------------

main()