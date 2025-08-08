import os
import shutil
import re

directory = os.path.join(r"C:\\", input("Enter base folder: "), input("Enter subfolder name: "))


if not os.path.isdir(directory):
    print(f"The directory '{directory}' does not exist.")
else:
    folders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]

    
    sort_type = input("Sort folders alphabetically or numerically? (a/n): ").lower()

    if sort_type == 'n':
    
        def numeric_key(name):
            match = re.match(r'^(\d+)', name)
            return int(match.group(1)) if match else float('inf')

        folders.sort(key=numeric_key)
    elif sort_type == "a":
        num_order = input("Numbers first or last? (f/l): ").lower()

        def numbers_first(name):
            match = re.match(r'^\D*(\d+)', name)
            return (0, int(match.group(1))) if match else (1, name.lower())

        def letters_first(name):
            match = re.match(r'^\D*(\d+)', name)
            return (1, int(match.group(1))) if match else (0, name.lower())

        if num_order == "f":
            folders.sort(key=numbers_first)
        else:  # default: numbers last
            folders.sort(key=letters_first)
          

    print("Sorted folders:")
    for folder in folders:
        print(folder)
        