from datetime import datetime

PATH = '../exports/'

def export_to_txt(statistics: dict):
    export_name = statistics['filename'] + '_results.txt'

    print(f'Results exported to {PATH}{export_name}')
    print('Results saved in simple text format - easy to read and understand!')

    try:
        with open(PATH + export_name, 'w') as file:
            file.write('============================================================\n')
            file.write('\tTEXT ANALYSIS RESULTS\n')
            file.write('============================================================\n')

            file.write(f'File analysed: {statistics['filename']}\n')
            file.write(f'Analysis date: {datetime.now().strftime('%Y-%m-%d')}\n\n')

            file.write('BASIC STATISTICS\n')
            file.write('--------------------\n')


    except IOError:
        print('There was an error writing to file!')
    return None