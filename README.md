# Brutus

Multi-character code generator in pure unadulterated Python.

1. Install termcolor: `pip install termcolor`

2. `git clone https://github.com/simonkeng/brutus.git`

3. Tune `options`, `k_value`, and `iterations` to generate your desired code.

For example, if you wanted a 6 character code, all uppercase, containing only the letters `A` through `F`, no numbers. The possibilities are 6 options raised to the number of characters in the code, `6 ** 6 = 46656` possible unique combinations. Through some test runs you can tune `iterations` to be large enough for `random.choices()` to find all the unique codes.


```python
def build(options, k_value, iterations):
    # algorithm
    return 'data.txt'

# with --wordscape the output from
# build() will be parsed by the
# US english dictionary, all the resulting
# (if any) english words will
# be writen to results.txt


if __name__ == "__main__":
   build("ABCDEF", 6, 180000)

```

