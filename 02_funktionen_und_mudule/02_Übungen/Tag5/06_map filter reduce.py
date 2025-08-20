# Ü1
# def uppercase_word(text):
#     uppercase_text = text.upper()
#     return uppercase_text

# words = ["python", "lernen", "macht", "spaß"]
# ergebnis = map(uppercase_word, words)
# print(list(ergebnis))


# Ü2
# # def filter_even_numbers(x):
# #     if x % 2 == 0:
# #         return x
# y = lambda x: x % 2 == 0
# orignal = [5, 7, 8, 13, 6, 10]
# # gefilter = filter(filter_even_numbers, orignal)
# gefilter = filter(y, orignal)
# print(list(gefilter))

# Ü3
# y = lambda x: x ** 2
# original = [3, 5, 9]
# result = map(y, original)
# print(list(result))

# Ü4
def filter_words(word, letter):
    return filter(lambda word: word.lower().startswith(letter.lower()), word)

words = ["Apfel", "Banane", "Avocado", "Blaubeere", "Aprikose"]
result = filter_words(words, 'b')
print(list(result))