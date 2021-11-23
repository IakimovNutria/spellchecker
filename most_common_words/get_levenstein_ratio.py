from fuzzywuzzy import process
from get_most_common_words import get_most_common_words, get_most_common_words_dict

lol = get_most_common_words(get_most_common_words_dict())
a = process.extract("кость", lol, limit=1)
print(a)
