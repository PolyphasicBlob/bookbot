def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


from stats import count_words


def main():
    wordcount = count_words(get_book_text("books/frankenstein.txt"))
    print(f"Found {wordcount} total words")


main()
