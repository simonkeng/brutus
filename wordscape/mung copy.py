import enchant
from termcolor import colored

dictionary = enchant.Dict("en_US")

eng_words = list()

with open('data.txt', 'r') as f:
    raw_str = f.read()
    inter_str = raw_str.split('{')[1]
    data_list = inter_str.split('}')[0].split(',')

    for word in data_list:
        word = word.lstrip()
        word = word.lstrip("'")
        word = word.rstrip("'")

        if dictionary.check(word):
            print('English word found! ', colored(word, 'green'))
            eng_words.append(word)

        else:
            print('Not an english word: ', colored(word, 'red'))


with open('english_words.txt', 'w') as g:
    g.write(str(eng_words))
