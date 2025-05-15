import sys
from stats import get_num_words, find_unique_chars, chars_dict_to_sorted_list

# Use path in script rather than hard code
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# Set book_path variable to the first argument passed to the script. (0 arg is the name of the file)
book_path = sys.argv[1]

def main():
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = find_unique_chars(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print(sys.argv)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def get_book_text(filepath ):
    with open(filepath ) as f:
        return f.read()

main()