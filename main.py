import sys
from stats import word_count, char_count, print_sorted

if (len(sys.argv) == 1):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book = sys.argv[1]

# The get_book_text function reads a file and returns all text as a string
def get_book_text(book):
    book_text = ""
    with open(book) as f:
        book_text = f.read()
    return book_text


def main():
    text = get_book_text(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print(f"Found {word_count(text)} total words")
    #print(char_count(text))
    print("--------- Character Count -------")
    sorted_chars = print_sorted(char_count(text))
    for item in sorted_chars:
        char = item["char"]
        count = item["count"]
        print(f"{char}: {count}")
    print("============= END ===============")
    #print("Type of char_count:", type(char_count))
    #print("Value of char_count:", char_count)
    #print(print_sorted(char_count(text)))

main()

