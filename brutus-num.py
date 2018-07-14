import numpy as np
from termcolor import colored

store = list()

options = 'A B C D E F'
options = options.split(' ')
size = 6
count = 0

while True:

    guess = np.random.choice(options, size=size)
    guess = guess.tolist()
    guess = ''.join(guess)

    if guess not in store:
        print('New unique code generated', colored(guess, 'green'))
        store.append(guess)
        count += 1
        print('Count:', count)

    else:
        print('Code already found:', colored(guess, 'red'))
        print('Count:', count)


    if len(store) == size ** len(options):

        # save results
        with open('num-data.txt', 'w') as f:
            f.write(str(store))
            f.write(str(len(store)))

        print('finished:', len(store))
        break


