import requests

# function to get meaning of the word


def get_meaning(word):
    try:
        resp = requests.get(
            'https://api.dictionaryapi.dev/api/v2/entries/en_US/{}'.format(word))
        resp_json = resp.json()
        type = resp_json[0]["meanings"][0]["partOfSpeech"]
        meaning = resp_json[0]["meanings"][0]["definitions"][0]["definition"]

        return type, meaning
    except Exception as e:
        print("exception occured: ", e)


if __name__ == "__main__":
    word = input("Word? ")
    if word != "":
        type, meaning = get_meaning(word)
        print(f"{word}. {type}. {meaning}")
    else:
        print("please enetr a valid word to be searched")

