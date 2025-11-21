import sys

if len(sys.argv) <= 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import count_characters, count_words, sort_chara_dictionary


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    words_counted = count_words(get_book_text(sys.argv[1]))
    print(f"Found {words_counted} total words")
    print("--------- Character Count -------")
    final_count = sort_chara_dictionary(count_characters(get_book_text(sys.argv[1])))
    for letter in final_count:
        if letter["char"].isalpha():
            print(f"{letter['char']}: {letter['num']}")
        else:
            continue


main()
