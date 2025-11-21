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
    sorted_characount = []

    for ch in characount:
        if ch in sorted_characount:
            sorted_characount[ch] += 1
        else:
            sorted_characount.append({"char": ch, "num": 1})

    return sorted_characount
