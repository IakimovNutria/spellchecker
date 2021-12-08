import argparse

from fuzzywuzzy import fuzz

from most_common_words.utils import get_most_common_words, \
    get_most_common_words_dict, get_colored_diff

most_common_words_list = get_most_common_words(get_most_common_words_dict())
most_common_words_set = set(most_common_words_list)


def spell_check(word):
    if word not in most_common_words_set:
        for common_word in most_common_words_list:
            if fuzz.ratio(word, common_word) >= percent:
                print(
                    f'{word} invalid,'
                    f' correct word: {get_colored_diff(word, common_word)}',
                    file=output)
                break
        else:
            print(
                f"{word} invalid."
                f" Don't know how to correct a word with precision {percent}",
                file=output)
    else:
        print(f'{word} valid', file=output)


def check_word(word):
    if args.regex:
        import re
        try:
            print(re.sub(args.regex[0], args.regex[1], word), end=' ', file=output)
        except re.error:
            print("Regex pattern error")
            exit(0)
    else:
        good_word = word
        for s in bad_symbols:
            good_word = good_word.replace(s, '')
        spell_check(good_word)


parser = argparse.ArgumentParser()
parser.add_argument("words", type=str, help="Sentence (words) for spell check",
                    metavar="WORD", nargs='*')
parser.add_argument("-p", "--precision", type=float, default=80,
                    metavar='PERCENTS', required=False,
                    help="precision of searching in percents (default=80)")
parser.add_argument("-r", "--regex", type=str, metavar='PATTERN',
                    required=False, nargs=2,
                    help="regex mode for spell replace")
parser.add_argument("-i", "--input", type=str, metavar='FILENAME',
                    required=False,
                    help="input file to read and spell check")
parser.add_argument("-o", "--output", type=str, metavar='FILENAME',
                    required=False,
                    help="output file to write output")
args = parser.parse_args()

percent = args.precision
bad_symbols = ['.', ',', '?', '!', '\n']
sentence = args.words
output = None
if args.output:
    output = open(args.output, 'w')
if args.input:
    try:
        with open(args.input, 'r') as f:
            for line in f:
                for word in line.split():
                    check_word(word)
    except OSError as err:
        print(f"Input file error: {err}")
for word in sentence:
    check_word(word)
if output:
    output.close()
print()
