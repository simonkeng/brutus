# Brutus

Multi-character code generator in Python 3.6

1. Install termcolor: `pip install termcolor`

2. `git clone https://github.com/simonkeng/brutus.git`

3. Tune `options`, `iterations`, and `k` to generate your desired code. 

For example:

```python
# for a 3 letter code, ascii uppercase, alphabetical
# 26 letters in the alphabet, 3 letters per code
# 26^3 = 17,576 possibilities

# alphabetical uppercase
options = string.ascii_uppercase

# to give random.choices() extra time to find 
# all 17 thousand possible codes (through trail & error)
# i've found that 300 thousand is necessary
# to reproducibly find them all.
iterations = 300000

# then set k to 3
random.choices(options, k=3)

```

