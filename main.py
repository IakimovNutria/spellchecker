import argparse
import colorama
from fuzzywuzzy import fuzz

from most_common_words.utils import get_most_common_words, get_most_common_words_dict


most_common_words_list = get_most_common_words(get_most_common_words_dict())
most_common_words_set = set(most_common_words_list)


def spell_check(word):
    if word not in most_common_words_set:
        for common_word in most_common_words_list:
            if fuzz.ratio(word, common_word) >= percent:
                print(f'{word} invalid, correct word: {common_word}')
                break
        else:
            print(f"{word} invalid. Don't know how to correct a word with precision {percent}")
    else:
        print(f'{word} valid')

def get_colored_diff(original, correct):
    pass


parser = argparse.ArgumentParser()
parser.add_argument("words", type=str, help="Sentence (words) for spell check", metavar="WORD", nargs='+')
parser.add_argument("-p", "--precision", type=float, default=80, metavar='PERCENTS', required=False,
                    help="precision of searching in percents (default=80)")
args = parser.parse_args()

percent = args.precision
bad_symbols = ['.', ',', '?', '!']
sentence = args.words
for word in sentence:
    good_word = word
    for s in bad_symbols:
        good_word = good_word.replace(s, '')
    spell_check(good_word)




