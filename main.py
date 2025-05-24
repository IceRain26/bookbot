from stats import get_num_words, count_characters, statistics
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")
get_num_words(book_path)
print("----------- Character Count -----------")
statistics(book_path)
print("============= END ===============")
