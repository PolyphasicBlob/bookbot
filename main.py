from stats import count_characters, count_words, sort_chara_dictionary


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    words_counted = count_words(get_book_text("books/frankenstein.txt"))
    print(f"Found {words_counted} total words")
    print("--------- Character Count -------")
    characters_counted = count_characters(get_book_text("books/frankenstein.txt"))
    print(characters_counted)
    final_count = sort_chara_dictionary(
        count_characters(get_book_text("books/frankenstein.txt"))
    )
    print(final_count)


main()
