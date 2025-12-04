import sys
from stats import get_num_words, get_num_chars, get_sorted_dict

def get_book_text(path):
    with open(path, 'r') as file:
        file_content = file.read()
        return file_content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    file_content = get_book_text(path)
    num_words = get_num_words(file_content)
    num_chars = get_num_chars(file_content)
    sorted_chars = get_sorted_dict(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for chars in sorted_chars:
        if chars['char'].isalpha():
            print(f"{chars['char']}: {chars['num']}")
    print("============= END ===============")

main()
