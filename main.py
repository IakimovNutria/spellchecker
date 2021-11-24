import argparse
from most_common_words.utils import get_most_common_words, get_most_common_words_dict
from fuzzywuzzy import process
from fuzzywuzzy import fuzz

parser = argparse.ArgumentParser()
parser.add_argument("word", type=str, help="word for spell check", metavar="WORD")
parser.add_argument("-p", "--precision", type=float, default=80, metavar='PERCENTS', required=False, help="precision of searching in percents (default=80)")
args = parser.parse_args()

percent = args.precision
word = args.word
most_common_words_list = get_most_common_words(get_most_common_words_dict())
most_common_words_set = set(most_common_words_list)
if word not in most_common_words_set:
    for common_word in most_common_words_list:
        if fuzz.ratio(word, common_word) >= percent:
            print('Word invalid, correct word:', common_word)
            break
    else:
        print(f"Word invalid. Don't know how to correct a word with precision {percent}")
else:
    print('Word valid')




