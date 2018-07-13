import os, sys, time
import string
import random
import enchant
from termcolor import colored


def build(options, k_value, iterations):

    ### param parsing & calculating

    opt_val = len(options)
    k_val = k_value
    combos = opt_val ** k_val

    ### info text

    print(colored('Brutus initialized..', 'yellow'))
    time.sleep(1)
    print('Calculated number of iterations needed:')
    print(opt_val, '**', k_val, '=', combos)
    time.sleep(1)
    print(colored('Brutus ready..', 'cyan'))
    time.sleep(4)

    ### -->  MAIN  <-- ###

    store = dict()
    itr = 0

    for i in range(iterations):

        guess_list = random.choices(options, k=k_value)
        guess = ''.join(guess_list)
        itr += 1

        if guess not in store.values():

            store[itr] = guess
            print('New unique code found & saved: ', colored(guess, 'green'))
            print('On iteration: ', itr)

        else:
            print('Code already found: ', colored(guess, 'red'))
            print('On iteration: ', itr)



    final = set(store.values())
    print('Final number of unique codes found: ', len(final))
    print(colored('Writing results to data.txt', 'yellow'))

    with open('data.txt', 'w') as f:
        f.write(str(final))



def munge(input_file):

    dictionary = enchant.Dict("en_US")
    eng_words = list()

    with open(input_file, 'r') as f:

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


    with open('results.txt', 'w') as g:
        g.write(str(eng_words))



if __name__ == "__main__":
    build("LYEST", 3, 3000)

    try:
        if 'data.txt' in os.listdir(os.getcwd()) and sys.argv[1] == '--wordscape':
            munge('data.txt')

    except IndexError:
        sys.exit()


