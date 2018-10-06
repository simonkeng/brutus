import os, sys, time
import argparse
import string
import random
import pickle
import enchant
from termcolor import colored

# parser = argparse.ArgumentParser()

# parser.add_argument('options', help='Options as string')


def generate(options, k_value):

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

    store = list()
    itr = 0

    while True:

        guess_list = random.choices(options, k=k_value)
        guess = ''.join(guess_list)

        if guess not in store:

            store.append(guess)
            itr += 1
            print('New unique code found & saved: ', colored(guess, 'green'))
            print('Unique codes found: ', itr)

        else:
            print('Code already found: ', colored(guess, 'red'))
            print('Unique codes found: ', itr)


        if len(store) == len(options) ** k_value:

            print('Final number of unique codes found: ', len(store))
            print(colored('Writing results to data.txt & pickle file.', 'yellow'))


            with open('tests/data.pkl', 'wb') as f:
                pickle.dump(store, f)

            # write out human readable version
            with open('tests/data.txt', 'w') as g:
                g.write(str(store))
                g.write(str(len(store)))

            break


def munge(input_file):

    dictionary = enchant.Dict("en_US")
    eng_words = list()

    with open(input_file, 'rb') as f:
        code_list = pickle.load(f)

        for code in code_list:

            if dictionary.check(code):
                print('English code found! ', colored(code, 'green'))
                eng_words.append(code)

            else:
                print('Not an english word: ', colored(code, 'red'))

    with open('tests/results.txt', 'w') as g:
        g.write(str(eng_words))


if __name__ == "__main__":
    generate('ASEGHOPLM', 5)

    try:
        if 'data.txt' in os.listdir(os.getcwd()) and sys.argv[1] == '--wordscape':
            munge('tests/data.pkl')
    except IndexError:
        sys.exit()

