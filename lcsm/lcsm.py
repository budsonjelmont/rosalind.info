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
    for index, record in enumerate(SeqIO.parse(handle, "fasta")):
        # print(record.id)
        # print(record.name)
        seqs[index] = record.seq

match_dict = {}


def iter_seqs(postuple):
    for i in range(len(postuple)):
        if postuple[i] + 1 < len(seqs[i]):
            iter_seqs(
                tuple(
                    postuple[j] if j != i else postuple[j] + 1
                    for j in range(len(postuple))
                )
            )
    lastchar = None
    allmatch = True
    for i in range(len(postuple)):
        currentchar = seqs[i][postuple[i]]
        if not lastchar:
            lastchar = currentchar
        elif lastchar == currentchar:
            continue
        else:
            allmatch = False
            break
    if allmatch:
        # if False in [i - 1 >= 0 for i in postuple]:
        score = 1
        # else:
        #     score = match_dict[tuple(i - 1 for i in postuple)] + 1
    else:
        score = 0
    match_dict[postuple] = score


iter_seqs(tuple(0 for i in range(len(seqs))))


def find_substr(coords, substr):
    if match_dict[coords] == 1:
        newsubstr = seqs[0][coords[0]] + substr
        if not False in [i - 1 >= 0 for i in coords]:
            return find_substr(tuple([i - 1 for i in coords]), newsubstr)
        else:
            return substr
    else:
        return substr


len_longest_match = 0
longest_match = ""

for coords, match in match_dict.items():
    substr = find_substr(coords, "")
    if len(substr) > len_longest_match:
        len_longest_match = len(substr)
        longest_match = substr

print(f"longest_match: {longest_match}")
print(f"len_longest_match: {len_longest_match}")
