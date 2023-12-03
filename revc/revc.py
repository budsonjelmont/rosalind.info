# Problem

# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

# The reverse complement of a DNA string s
# is the string sc formed by reversing the symbols of s

# , then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

# Given: A DNA string s

# of length at most 1000 bp.

# Return: The reverse complement sc
# of s

# .
# Sample Dataset

# AAAACCCGGT

# Sample Output

# ACCGGGTTTT

import sys

infile = sys.argv[1]

bpmap = {'A':'T','C':'G','G':'C','T':'A'}

with open(infile, 'r') as f:
    s = f.read().strip()

sc=''
for nuc in s[::-1]:
    sc += bpmap[nuc]

print(sc)

if len(sys.argv)>2:
    outfile = sys.argv[2]
    with open(outfile, 'w+') as f:
        f.write(sc)
