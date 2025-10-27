from string import printable
import load
import time
import display
import export


def main():
    flag = True
    statistics = {
        "filename": ""
    }  # dictionary containing statistics for the whole book, after we selected it

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
        print(
            f"\t{('Current file: ' + statistics['filename']) if statistics['filename'] != '' else 'No file loaded'}"
        )

        choice = input(
            "\n\tInsert your choice (0 - 6): "
        )  # TODO: handle user input, also None case

        # TODO: If the book is not loaded yet, there is no point in accessing any
        # menu other than the 1st one.
        match choice:
            case "1":
                statistics = load.load_file()
            case "2":
                display.basic_statistics(statistics)
            case "3":
                display.word_analysis(statistics)
            case "4":
                display.sentence_analysis(statistics)
            case "5":
                display.character_analysis(statistics)
            case "6":
                export.export_results(statistics)
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
