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

