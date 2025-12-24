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

def pairwise_aln(seq1,seq2):
    mtx = [[0 for j in seq2] for i in seq1]
    for ix1 in range(0,len(seq1)):
        for ix2 in range(0,len(seq2)):
            if seq1[ix1] == seq2[ix2]:
                if ix1 > 0 and ix2 > 0:
                    mtx[ix1][ix2] = max(0, mtx[ix1-1][ix2-1])+1
                else:
                    mtx[ix1][ix2] = 1
    return mtx

# Get just the last positions of contiguous matches
def get_aln_last_pos(mtx):
    last_pos = []
    for ix1 in range(0,len(mtx)):
        for ix2 in range(0,len(mtx[ix1])):
            if mtx[ix1][ix2] > 0: # if there's a match at this position 
                if ix1+1 == len(mtx) or ix2+1 == len(mtx[ix1]): # if the match can't be extended because you're at a sequence boundary already
                    last_pos += [(ix1, ix2)]
                elif mtx[ix1+1][ix2+1] == 0: # if the match wasn't extended because next position was mismatchs
                    last_pos += [(ix1, ix2)]
    return last_pos

def find_substr(mtx, coords, seq, substr):
    substr = seq[coords[0]] + substr
    prevcoords = tuple([i - 1 for i in coords])
    if all([ix >= 0 for ix in prevcoords]):
        if mtx[prevcoords[0]][prevcoords[1]] > 0:
            return find_substr(mtx, prevcoords, seq, substr)
        else:
            return substr
    else:
        return substr

candidates = [seqs[0]]

for seq in seqs[1:]:
    remaining_candidates = []
    for candidate in candidates:
        mtx = pairwise_aln(candidate, seq)
        last_pos = get_aln_last_pos(mtx)
        matches = [ find_substr(mtx, t, candidate, "") for t in last_pos ]
        remaining_candidates += matches
    candidates = set(remaining_candidates)

longest_match = None
len_longest_match = 0
for substr in candidates:
    if len(substr) > len_longest_match:
        longest_match = substr
        len_longest_match = len(substr)

print(f"longest_match: {longest_match}")
print(f"len_longest_match: {len_longest_match}")
