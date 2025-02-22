import re
import sys

def read_file(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def word_count(text):
    return len(text.split())


def character_count(text):
    chars = {}
    lowered = text.lower()
    for char in lowered:
        if char not in chars:
            chars[char] = 0
        chars[char] += 1
    return chars


def count_for(character, count):
    return f"The '{character}' character was found {count} times"


def print_report(file):
    text = read_file(file)
    character_map = character_count(text)
    print(f"--- Begin report of {file} ---")
    print(f"{word_count(text)} words found in the document")
    print("")
    for entry in character_map:
        if re.match(r"[a-z]", entry):
            print(count_for(entry, character_map[entry]))


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print_report(sys.argv[1])


main()
