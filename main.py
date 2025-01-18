import re


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


def print_report(text):
    character_map = character_count(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(text)} words found in the document")
    print("")
    for entry in character_map:
        if re.match(r"[a-z]", entry):
            print(count_for(entry, character_map[entry]))


def main():
    path = "./books/frankenstein.txt"
    text = read_file(path)
    print_report(text)


main()
