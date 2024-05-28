import sys
import os
import re
import argparse


def main():
    user = os.path.expanduser("~")
    dir = os.path.join(user, "Downloads")
    pattern = r'^TB_.*\.(mp4|png)$'

    if len(sys.argv) > 1:
        args = argument_parse()
        dir = args.dir_path
        pattern = args.search_pattern
    
    files = check_for_files(dir, pattern)
    
    print(f"Found {len(files)} files, ")
    if len(files) == 0:
        sys.exit(0)
    user_input = input("Press d to delete files\nPress n to do nothing\n")
    
    if user_input == 'd':
        deleteFiles(dir, files)
    
    sys.exit(0)

def argument_parse():
    parser = argparse.ArgumentParser(description="process arguments and flags")

    parser.add_argument('dir_path', type=str, nargs='?', help="Specify path to working directory")
    parser.add_argument('search_pattern', type=str, nargs='?', help="RegEx pattern to match files")

    args = parser.parse_args()

    return args

def check_for_files(directory, pattern):
    compiled_pattern = re.compile(pattern)

    try:
        files = os.listdir(directory)
    except FileNotFoundError:
        print(f"The directory {directory} does not exist")
        sys.exit(5)
    
    matched_files = []

    for filename in files:
        if compiled_pattern.match(filename):
            matched_files.append(filename)

    return matched_files

def deleteFiles(path, files):
    try:
        for file in files:
            file_path = os.path.join(path, file)
            os.remove(file_path)
    except PermissionError:
        print(f"Permission denied: Cannot delete {file}.")
        sys.exit(6)
    except OSError as e:
        print(f"Error deleting file {file}: {e}")
        sys.exit(7)

if __name__ == "__main__":
    main()