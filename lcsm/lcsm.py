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

infile = sys.argv[1]

seqs = []

with open(infile) as handle:
    for ix, record in enumerate(SeqIO.parse(handle, "fasta")):
        # print(record.id)
        # print(record.name)
        seqs.append(record.seq)


def check_pos(coords, aln_seqs):
    '''
    '''
    seqix = len(coords)
    if seqix < len(aln_seqs): # if there are other seqs not traversed yet
        for charix in range(0,len(aln_seqs[seqix])): # each basepair in seq with index ix
            check_pos(coords + (charix,), aln_seqs) # recurse by calling check_pos() again on the next sequence with each position in the current sequence
    else:
        if all([d[0][d[1]]==aln_seqs[0][coords[0]] for d in zip(aln_seqs, coords)]): ## if all sequences match at this position
            prevcoords = tuple([i - 1 for i in coords])
            if all([ix >= 0 for ix in prevcoords]) and prevcoords in pos_scores: # if there's a previous position is still inside the sequence space
                pos_scores[coords] = pos_scores[prevcoords] + 1
            else:
                pos_scores[coords] = 1
        # else:
        #     pos_scores[coords] = 0
        return

def find_substr(coords, seq, substr):
    substr = seq[coords[0]] + substr
    prevcoords = tuple([i - 1 for i in coords])
    if all([ix >= 0 for ix in prevcoords]):
        if prevcoords in pos_scores:
            return find_substr(prevcoords, seq, substr)
        else:
            return substr
    else:
        return substr

candidates = [seqs[0]]

pos_scores = {}

for seq in seqs[1:]:
    remaining_candidates = []
    for candidate in candidates:
        pos_scores = {}
        check_pos((),[seq,candidate])
        for coords in pos_scores: # for every scored position
            substr = find_substr(coords, seq, "")
            if substr not in remaining_candidates:
                remaining_candidates.append(substr)
    candidates = remaining_candidates

longest_match = None
len_longest_match = 0
for substr in candidates:
    if len(substr) > len_longest_match:
        longest_match = substr
        len_longest_match = len(substr)

print(f"longest_match: {longest_match}")
print(f"len_longest_match: {len_longest_match}")
