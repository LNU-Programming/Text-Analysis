import os



def file_loading():
    print("\n--- File Selection ---\nAvailable text files:")
    # TODO: If no files ar present, return nothing
    for index, x in enumerate(os.listdir('../data/')):
        if x.endswith(".txt"):
            # Prints only text file present in My Folder
            print(f'{index+1}) {x}')

    # TODO: Input checking properly
    flag = True
    choice = 0
    while True:
        choice = int(input("Enter a number from the list above. "))
        selected_file = os.listdir('../data/')
        if 0 < choice < len(selected_file):
            # TODO: call file analysis
            return selected_file[choice-1]
        else:
            print("Please choose an appropriate number.")