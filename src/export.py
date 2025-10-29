PATH = '../exports/'

def export_to_txt(statistics: dict):
    export_name = statistics['filename'] + '_results.txt'

    print(f'Results exported to {PATH}{export_name}')
    print('Results saved in simple text format - easy to read and understand!')

    try:
        with open(PATH + export_name, 'w') as file:
            file.write('Ciao mi chiamo fagiolo\n')
            file.write('Ciaoissimooo\n')
            file.write('Cia cia')
    except IOError:
        print('There was an error writing to file!')
    return None