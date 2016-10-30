from collections import defaultdict
import os

def find_duplicates(root_directory):
    dup_files = defaultdict(list)
    for dirpath, dirnames, files in os.walk(root_directory):
        for filename in files:
            full_file_path = os.path.join(dirpath, filename)
            file_size = os.stat(full_file_path).st_size
            dup_files[(filename, file_size)].append(full_file_path)
    return {key[0]: val for key, val in dup_files.items() if len(val) > 1}


def show_duplicates(duplicates_dict):
    for key, value in duplicates_dict.items():
        print('File "{0}" found in following directories:'.format(key))
        for v in value:
            print('    {0}'.format(v))

if __name__ == '__main__':
    show_duplicates(find_duplicates(input('Enter root directory: ')))
