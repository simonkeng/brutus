import string
import random
from termcolor import colored
import time

### -->  PARAMS  <-- ###

options = "RACWL"

k_value = 5

### ---------------- ###

### param parsing

opt_val = len(options)
k_val = k_value
posibles = opt_val ** k_val
iterations = round(posibles + (posibles / 2))

### TUI intro

print(colored('Brutus initialized..', 'yellow'))
time.sleep(1)
print('Calculated iterations needed with inflation:')
print(opt_val, '**', k_val, '=', iterations, 'noninflated:', posibles)
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


with open('data.txt', 'w') as f:
    f.write('Generated codes:\n')
    f.write(str(final))
    f.write('\nNumber of codes found:\n')
    f.write(str(len(final)))


### ---------------- ###
