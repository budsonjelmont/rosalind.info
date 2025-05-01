# Problem

# A common substring of a collection of strings is a substring of every member of the collection. 
# We say that a common substring is a longest common substring if there does not exist a longer common substring. 
# For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; 
# in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

# Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

# Given: A collection of k
# (k≤100

# ) DNA strings of length at most 1 kbp each in FASTA format.

# Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
# Sample Dataset

# >Rosalind_1
# GATTACA
# >Rosalind_2
# TAGACCA
# >Rosalind_3
# ATACA

# Sample Output

# AC

import sys
from Bio import SeqIO


infile = sys.argv[1]

lendict = {}
occurdict = {}

# TOO SLOW

with open(infile) as handle:
    for index, record in enumerate(SeqIO.parse(handle, "fasta")):
        # print(record.id)
        # print(record.name)
        nseqs += 1
        seq = record.seq
        minlen = len(seq) if len(seq) < minlen or minlen==0 else minlen
        for pos in range(0, len(seq)):
            iter_substrs(index, seq, '', pos, 0)

# print(lendict)
# print(occurdict)

found = False
for length in range(minlen, 0,-1):
    for subseq in lendict[length]:
        if len(occurdict[subseq])==nseqs:
            print(subseq)
            found = True
            break
    if found:
        break

if not found:
    print(None)