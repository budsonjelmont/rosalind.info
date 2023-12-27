# Problem

# After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

# Given: A DNA string s
# (of length at most 1 kbp) and a collection of substrings of s

# acting as introns. All strings are given in FASTA format.

# Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)

# Sample Dataset

# >Rosalind_10
# ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
# >Rosalind_12
# ATCGGTCGAA
# >Rosalind_15
# ATCGGTCGAGCGTGT

# Sample Output

# MVYIADKQHVASREAYGHMFKVCA

import sys
from Bio import SeqIO, Seq

infile = sys.argv[1]

dnas=None
intdct={}

with open(infile) as handle:
    for index, record in enumerate(SeqIO.parse(handle, "fasta")): 
        if index == 0:
            dnas = record.seq
        else:
            intdct[record.id] = record.seq

splcdnas=''
i = 0
while i < len(dnas):
    i_og = i
    for motif in intdct.values():
        motiflen = len(motif)
        if i+motiflen > len(dnas):
            continue
        else:
            if dnas[i:i+motiflen] == motif:
                i = i+motiflen
                break
    if i != i_og:
        continue
    else:
        splcdnas = splcdnas + dnas[i]
        i = i+1

# expected='ATGGTCTACATAGCTGACAAACAGCACGTAGCATCTCGAGAGGCATATGGTCACATGTTCAAAGTTTGCGCCTAG'
# if splcdnas == expected:
#     print('MATCHED')

aas = Seq.Seq(splcdnas).translate(to_stop=True)

if len(sys.argv)>2:
    outfile = sys.argv[2]
    with open(outfile, 'w+') as f:
        f.write(str(aas))