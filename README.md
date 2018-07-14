# Brutus

Multi-character code generator in pure unadulterated Python.

1. Install termcolor: `pip install termcolor`

2. `git clone https://github.com/simonkeng/brutus.git`

3. Tune `options` and `k_value` to generate your desired code.

> options = what the code consists of (`'ABCD'`, `123456`,`['bob', 'ann', 'dan']`)

> k_value = size of the code (4 characters long, 6-digits, single, etc.)

For example, if you wanted a 6 character code, all uppercase alphabetical, no numbers. The possibilities are 26 options (A through Z) raised to the number of characters in the code (6 in this example), `26 ** 6 = 308915776` possible unique combinations. All 300 million combinations will be written to `data.txt`, for readability but will also be saved as binaries (`data.pkl`). 

Another example is using this algorithm to solve word puzzles (like [wordscapes](https://itunes.apple.com/ca/app/wordscapes/id1207472156?mt=8)) you can run the script with `--wordscape` (`python brutus.py --wordscape`) to read those binaries back into memroy then sanitized though the english dictionary ([pyenchant](https://github.com/rfk/pyenchant)) to collect any english words found in your list of generated codes. 


```python
def generate(options, k_value):
    # algorithm

if __name__ == "__main__":
    generate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 6)

```

**Disclaimer:** 
In the first example, generating 308 million unique 6-char codes would take an insane
amount of time on any average local machine. Generate at your own risk. 
