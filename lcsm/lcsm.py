# Problem

# A common substring of a collection of strings is a substring of every member of the collection.
# We say that a common substring is a longest common substring if there does not exist a longer common substring.
# For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible;
# in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

# Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

# Given: A collection of k
# (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

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
import numpy as np

infile = sys.argv[1]

seqs = {}

with open(infile) as handle:
    for ix, record in enumerate(SeqIO.parse(handle, "fasta")):
        # print(record.id)
        # print(record.name)
        seqs[ix] = record.seq

all_coords = []
pos_scores = np.ndarray([len(s) for s in seqs.values()], int)

def check_pos(coords):
    '''
    '''
    seqix = len(coords)
    if seqix < len(seqs): # if there are other seqs not traversed yet
        for charix, char in enumerate(seqs[seqix]):  # each basepair in seq with index ix
            check_pos(coords + (charix,)) # recurse by calling check_pos() again on the next sequence with each position in the current sequence
    else:
        all_coords.append(coords)
        if all([seqs[d[0]][d[1]]==seqs[0][coords[0]] for d in zip(seqs, coords)]): ## if all sequences match at this position
            if all([ix-1 >= 0 for ix in coords]): # if there's a previous position is still inside the sequence space
                pos_scores[coords] = pos_scores[tuple([ix-1 for ix in coords])] + 1
            else:
                pos_scores[coords] = 1
        else:
            pos_scores[coords] = 0
        return

check_pos(()) # start with empty tuple

def find_substr(coords, substr):
    substr = seqs[0][coords[0]] + substr
    nextcoords = tuple([i - 1 for i in coords])
    if all([ix-1 >= 0 for ix in nextcoords]):
        if pos_scores[nextcoords]> 0:
            return find_substr(nextcoords, substr)
        else:
            return substr
    else:
        return substr

len_longest_match = 0
longest_match = ""

for coords in all_coords: # for every scored position
    if pos_scores[coords] > 0:
        substr = find_substr(coords, "")
        if len(substr) > len_longest_match:
            len_longest_match = len(substr)
            longest_match = substr

print(f"longest_match: {longest_match}")
print(f"len_longest_match: {len_longest_match}")
