import string
import random
from termcolor import colored

# 26 letters
options = string.ascii_uppercase

store = dict()
itr = 0

# 100,000 iterations
iterations = 300000

for i in range(iterations):

    # k=3 for 3 letter codes
    guess_list = random.choices(options, k=3)
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
