
import sys
from stats import count_words, count_characters, sort_character_couns

def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        contents = f.read()
        return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")

    contents = get_book_text(file_path)
    word_count = count_words(contents)
    char_count = count_characters(contents)
    char_count_sorted = sort_character_couns(char_count)

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, count in char_count_sorted:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()
