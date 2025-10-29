PATH = '../exports/'

def export_to_txt(statistics: dict):
    export_name = statistics['filename'] + '_results.txt'

    print(f'Results exported to {PATH}{export_name}')
    print('Results saved in simple text format - easy to read and understand!')



    return None