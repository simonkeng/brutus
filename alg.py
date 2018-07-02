import string
import random
from termcolor import colored

options = string.ascii_uppercase

store = dict()
itr = 0

# 500,000 iterations to find them all
iterations = 500000

for i in range(iterations):

    guess_list = random.choices(options, k=3)
    guess = ''.join(guess_list)
    itr += 1

    if guess not in store.values():

        store[itr] = guess
        print('New code found & added to store: ', colored(guess, 'green'))


    else:
        print('Already in store: ', colored(guess, 'red'))

final = set(store.values())

print('Final store size: ', len(final))

with open('store.txt', 'w') as f:
    f.write(str(final))
    f.write('\nSize of store:\n')
    f.write(str(len(final)))
