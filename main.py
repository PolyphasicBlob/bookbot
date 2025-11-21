def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


def count_words(file_contents):
    wordcount = len(file_contents.split())
    print(wordcount)
    return wordcount


def main():
    return count_words(get_book_text("books/frankenstein.txt"))


main()
