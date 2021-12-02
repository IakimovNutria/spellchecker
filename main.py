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
                print(f'{word} invalid, correct word: {get_colored_diff(word, common_word)}')
                break
        else:
            print(f"{word} invalid. Don't know how to correct a word with precision {percent}")
    else:
        print(f'{word} valid')


def get_colored_diff(original, correct):
    result = ''
    for i in range(len(correct)):
        if i >= len(original):
            result += colorama.Fore.GREEN + correct[i]
            continue
        if original[i] == correct[i]:
            result += colorama.Fore.RESET + correct[i]
        else:
            result += colorama.Fore.YELLOW + correct[i]
    result += colorama.Fore.RESET
    return result


def check_word(word):
    if args.regex:
        import re
        try:
            print(re.sub(args.regex[0], args.regex[1], word), end=' ')
        except re.error:
            print("Regex pattern error")
            exit(0)
    else:
        good_word = word
        for s in bad_symbols:
            good_word = good_word.replace(s, '')
        spell_check(good_word)


parser = argparse.ArgumentParser()
parser.add_argument("words", type=str, help="Sentence (words) for spell check", metavar="WORD", nargs='*')
parser.add_argument("-p", "--precision", type=float, default=80, metavar='PERCENTS', required=False,
                    help="precision of searching in percents (default=80)")
parser.add_argument("-r", "--regex", type=str, metavar='PATTERN', required=False, nargs=2,
                    help="regex for spell replace")
parser.add_argument("-f", "--file", type=str, metavar='FILE_NAME', required=False, nargs=1,
                    help="file to read and check")
parser.add_argument("-o", "--file", type=str, metavar='FILE_NAME', required=False, nargs=1,
                    help="file to write output")
args = parser.parse_args()


percent = args.precision
bad_symbols = ['.', ',', '?', '!', '\n']
sentence = args.words
if args.file:
    f = open(str(args.file[0]), 'r')
    for line in f:
        for word in line.split():
            check_word(word)
for word in sentence:
    check_word(word)
print()
