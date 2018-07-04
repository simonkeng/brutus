import string
import random
from termcolor import colored

# S U N I O U S are the letters we were given
# 7 letters, 7 positions, 7^7 = 823,543 possible combinations
# NOTE: there are only 6 unique letters, but in the case 
# of wordscape crossword puzzles, we know that the second
# "S" will be present in the final word, so I'm using 7
# letters instead of 6 for the calculation.

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



final = set(store.values())
print('Final number of unique codes found: ', len(final))

with open('data.txt', 'w') as f:
    f.write('Generated codes:\n')
    f.write(str(final))
    f.write('\nNumber of codes found:\n')
    f.write(str(len(final)))

