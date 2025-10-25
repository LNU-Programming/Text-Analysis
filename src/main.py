import file_loading

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

        choice = input("\n\tInsert your choice (0 - 6): ")

        match choice:
            case "1":
                statistics["filename"] = file_loading.file_loading()
            case "2":
                print("Choice two!")
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

# ----------------------------------------------------------------------------------------------------------------------

main()