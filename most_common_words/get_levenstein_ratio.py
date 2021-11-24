from fuzzywuzzy import process
from fuzzywuzzy import fuzz
from utils import get_most_common_words, get_most_common_words_dict


percent = 80
word = 'кошло'
most_common_words_list = get_most_common_words(get_most_common_words_dict())
most_common_words_set = set(most_common_words_list)
if word not in most_common_words_set:
    for common_word in most_common_words_list:
        if fuzz.ratio(word, common_word) >= percent:
            print(common_word)
            break

