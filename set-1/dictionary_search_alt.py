from nltk.corpus import wordnet

# function to extract type and meaning of the word


def get_meaning(word):
    try:
        syns = wordnet.synsets(word)
        wtype_abb = syns[0].pos()

        # type of word
        if wtype_abb == "n":
            word_type = "noun"

        elif wtype_abb == "a":
            word_type = "adjective"

        elif wtype_abb == "v":
            word_type = "verb"

        # meaning of "word"
        meaning = syns[0].definition()
        return word_type, meaning
    except Exception as e: 
        print("exception occured: ", e)


if __name__ == "__main__":
    word = input("Word? ")
    type, meaning = get_meaning(word)
    print(f"{word}. {type}. {meaning}.")
