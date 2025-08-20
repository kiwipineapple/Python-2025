import string
def ohne_zeichen(text):
    text_ohne_zeichen = ''.join(char for char in text if char not in string.punctuation)
    return text_ohne_zeichen

def nur_woerter(text):
    text_ohne_zahl = [x.lower() for x in text if x not in string.digits]
    return ''.join(text_ohne_zahl)

