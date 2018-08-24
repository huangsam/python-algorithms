def get_nearby_chars(char):
    consonants = set(['c', 'b', 'h', 'k', 't', 'r'])
    vowels = set(['a', 'e', 'o', 'i', 'o', 'u'])
    if char in consonants:
        return consonants
    if char in vowels:
        return vowels
    return set()


def is_word(word):
    valid_words = set([
        'cat',
        'hat',
        'bat',
        'hot',
        'hut',
        'hit',
        'rut',
        'hi',
        'ho',
        'to',
        'but',
        'jar'
    ])
    if word in valid_words:
        return True
    return False


def nearby_permutations(word, index):
    if index > len(word) - 1:
        return set([''])

    sub_words = nearby_permutations(word, index + 1)
    nearby_letters = get_nearby_chars(word[index])
    permutations = set()

    for sub_word in sub_words:
        for letter in nearby_letters:
            permutations.add(letter + sub_word)
    return permutations


def nearby_words(word):
    result = set()
    if len(word) == 0:
        return result
    possible_words = nearby_permutations(word, 0)
    for possible_word in possible_words:
        if is_word(possible_word) is True:
            result.add(possible_word)
    return result


def main():
    not_sures = ["ki", "kat"]
    for not_sure in not_sures:
        print("Possible words for {}:".format(not_sure))
        for word in nearby_words(not_sure):
            print(word)


if __name__ == "__main__":
    main()
