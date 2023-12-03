#Problem

# An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

# Given a DNA string t
# corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u

# .
# Given: A DNA string t

# having length at most 1000 nt.

# Return: The transcribed RNA string of t
# .

import sys

infile = sys.argv[1]

nucs = ['A','C','G','T']
nuccounts = {k:0 for k in nucs}

with open(infile, 'r') as f:
    u = f.read()

t=''
for nuc in u:
    if nuc == 'T':
        t+='U'
    else:
        t+=nuc

print(t)

if len(sys.argv)>2:
    outfile = sys.argv[2]
    with open(outfile, 'w+') as f:
        f.write(t)
