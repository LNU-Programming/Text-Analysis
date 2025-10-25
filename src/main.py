def main():
    flag = True
    while flag:
        print("\t 1) Load a basic text file")
        print("\t 2) Display basic statistics")
        print("\t 3) Show word frequency analysis")
        print("\t 4) Display sentence analysis")
        print("\t 5) Display character analysis")
        print("\t 6) Export results")
        print("\t 0) Exit program")

        choice = input("\tInsert your choice: ")

        match choice:
            case "1":
                print("Choice one!")
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