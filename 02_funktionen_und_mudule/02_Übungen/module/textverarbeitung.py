def anzahl_woerter(text):
    word = text.split()
    return len(word)

def anzahl_buchstaben(text):
    i = 0
    for word in text:
        for letter in word:
            i += 1
    return i


def text_in_grossbuchstaben(text):
    for word in text:
        return word.upper()
