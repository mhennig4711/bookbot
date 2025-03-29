
from operator import itemgetter

def count_words(file_content: str) -> int:
    return len(file_content.split())

def count_characters(file_content: str):
    result = {}
    for char in file_content:
        char = char.lower()
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

def sort_character_couns(char_counts) -> tuple[str, int]:
    result = []
    for char, count in char_counts.items():
        result.append((char, count))
    result.sort(key=itemgetter(1), reverse=True)
    return result
