import sys
from stats import get_word_count, count_chars, sort_chars

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    word_count = get_word_count(get_book_text(sys.argv[1]))
   
    print("============ BOOKBOT ============")
    print(f"Analyzing book foudn at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    char_count = sort_chars(count_chars(get_book_text(sys.argv[1])))
    for char in char_count:
        print(f"{char["char"]}: {char["num"]}")
main()