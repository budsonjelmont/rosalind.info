# Problem
# Figure 2. The Hamming distance between these two strings is 7. Mismatched symbols are colored red.

# Given two strings s
# and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t

# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

# Return: The Hamming distance dH(s,t)

# Sample Dataset

# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT

# Sample Output

# 7

import sys

infile = sys.argv[1]

with open(infile, 'r') as f:
    s1 = f.readline().strip()
    s2 = f.readline().strip()

#s1 = 'GAGCCTACTAACGGGAT'
#s2 = 'CATCGTAATGACGGCCT'

hdist = 0
for i in range(0, len(s1)):
    if s1[i] != s2[i]:
        hdist += 1

print(hdist)

if len(sys.argv)>2:
    outfile = sys.argv[2]
    with open(outfile, 'w+') as f:
        f.write(str(hdist))