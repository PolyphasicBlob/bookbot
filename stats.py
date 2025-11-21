def count_words(file_contents):
    wordcount = len(file_contents.split())
    return wordcount


def count_characters(file_contents):
    characount = {}
    lowercase_file_contents = file_contents.lower()
    for character in lowercase_file_contents:
        if character in characount:
            characount[character] += 1
        else:
            characount[character] = 1
    return characount


def sort_chara_dictionary(characount):
    pass
