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

seqs = {}

with open(infile) as handle:
    for ix, record in enumerate(SeqIO.parse(handle, "fasta")):
        # print(record.id)
        # print(record.name)
        seqs[ix] = record.seq

occur_dict = {}

for ix, record in seqs.items():
    for i, c in enumerate(record):  # each basepair in seq with index ix
        if c not in occur_dict:
            occur_dict[c] = {
                seqsix: [] for seqsix in seqs.keys()
            }  # initialize dict with empty array of matching positions for each sequence, with outer dict keyed on the basepair & inner dict keyed on the sequence index
        occur_dict[c][ix].append(i)

match_list = []


def find_matching_pos(char, seqix, tuple):
    nextseqix = seqix + 1
    for occurrence in occur_dict[char][seqix]:
        if nextseqix < len(seqs):
            find_matching_pos(char, nextseqix, tuple + (occurrence,))
        else:
            match_list.append(tuple + (occurrence,))


for c in occur_dict.keys():
    find_matching_pos(c, 0, ())


def find_substr(coords, substr):
    substr = seqs[0][coords[0]] + substr
    nextcoords = tuple([i - 1 for i in coords])
    if nextcoords in match_list:
        return find_substr(nextcoords, substr)
    else:
        return substr


len_longest_match = 0
longest_match = ""

for coords in match_list:
    substr = find_substr(coords, "")
    if len(substr) > len_longest_match:
        len_longest_match = len(substr)
        longest_match = substr

print(f"longest_match: {longest_match}")
print(f"len_longest_match: {len_longest_match}")
