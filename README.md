# Brutus

Multi-character code generator in pure unadulterated Python.

1. Install termcolor: `pip install termcolor`

2. `git clone https://github.com/simonkeng/brutus.git`

3. Tune `options`, `k_value`, and `iterations` to generate your desired code.

For example, if you wanted a 6 character code, all uppercase, containing only the letters `A` through `F`, no numbers. The possibilities are 6 options raised to the number of characters in the code, `6 ** 6 = 46656` possible unique combinations. All the combinations will be written to `data.txt`, for readability but will also be saved as binaries (`data.pkl`). If you run the script with `--wordscape` (`python brutus.py --wordscape`) then those binaries will be read back into memroy and sanitized though the english dictionary ([pyenchant](https://github.com/rfk/pyenchant)) to collect any english words found in your list of generated codes. 


```python
def generate(options, k_value):
    # algorithm
    return 'data.txt'
    return ''

# with --wordscape the output from
# build() will be parsed by the
# US english dictionary, all the resulting
# (if any) english words will
# be writen to results.txt


if __name__ == "__main__":
    generate("ABCDEF", 6, 180000)

```

