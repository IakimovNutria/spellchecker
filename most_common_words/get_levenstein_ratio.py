from fuzzywuzzy import process
from fuzzywuzzy import fuzz
from get_most_common_words import get_most_common_words, get_most_common_words_dict

#print(fuzz.ratio('Привет мир', 'Привет мир')) - выведет процент соответствия

lol = get_most_common_words(get_most_common_words_dict())
a = process.extract("кость", lol, limit=1)
print(a)
