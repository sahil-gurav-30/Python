import os
import re
print("Name: Sahil\nUSN: 1AY24AI093")
def search_regex_in_txt_files():
    pattern = input("Enter a regular expression: ")
    try:
        regex = re.compile(pattern)
    except re.error:
        print("Invalid regular expression.")
        return
    txt_files = [file for file in os.listdir() if file.endswith('.txt')]
    for file_name in txt_files:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, 1):
                if regex.search(line):
                    print(f"[{file_name} - line {line_number}] {line.strip()}")
search_regex_in_txt_files()
