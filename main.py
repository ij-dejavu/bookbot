from stats import get_num_words, get_num_characters, get_sorted_characters
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_content = get_book_text(book_path)
    num_words = get_num_words(book_content)
    num_characters = get_num_characters(book_content)
    num_characters_list = get_sorted_characters(num_characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for num_characters in num_characters_list:
        for char, count in num_characters.items():
            if char.isalpha():
                print(f"{char}: {count}")

    print("============= END ===============")

if __name__ == "__main__":
    main()