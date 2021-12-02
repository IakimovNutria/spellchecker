import json
import re
import colorama


data_file_name = 'most_common_words/most_common_words.txt'
text_file_name = 'most_common_words/text.txt'


def save_data(data):
    file = open(data_file_name, mode='w')
    json.dump(data, file)
    file.close()


def get_most_common_words_dict():
    file = open(data_file_name, mode='r')
    data = json.load(file)
    file.close()
    return data


def get_most_common_words(d):
    return list(d.keys())


def update_most_common_words_dict():
    file = open(text_file_name, mode='r')
    most_common_words_dict = get_most_common_words_dict()
    for line in file:
        for word in line.split():
            word = word.lower()
            word = re.sub(r'[^\w\s]', '', word)
            if is_cyrillic(word):
                most_common_words_dict[word] = most_common_words_dict.get(word, 0) + 1
    save_data(dict(sorted(most_common_words_dict.items(), key=lambda x: x[1])[::-1]))


def is_cyrillic(text):
    return bool(re.search('^[а-яА-Я]+$', text))


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