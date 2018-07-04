import string
import random
from termcolor import colored

# 823,543

options = "SUNIOUS"

store = dict()
itr = 0

iterations = 900000

for i in range(iterations):

    guess_list = random.choices(options, k=7)
    guess = ''.join(guess_list)
    itr += 1

    if guess not in store.values():

        store[itr] = guess
        print('New unique code found & saved: ', colored(guess, 'green'))
        print('On iteration: ', itr)

    else:
        print('Code already found: ', colored(guess, 'red'))
        print('On iteration: ', itr)

    
    if iterations == 200000:
        with open('200k-check.txt', 'w') as f:
            fin = set(store.values())
            f.write(str(fin))

final = set(store.values())
print('Final number of unique codes found: ', len(final))

with open('data.txt', 'w') as f:
    f.write('Generated codes:\n')
    f.write(str(final))
    f.write('\nNumber of codes found:\n')
    f.write(str(len(final)))

