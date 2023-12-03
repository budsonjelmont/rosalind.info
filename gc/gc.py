# Problem

# The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.
# DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.
# In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
# Sample Dataset

# >Rosalind_6404
# CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
# TCCCACTAATAATTCTGAGG
# >Rosalind_5959
# CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
# ATATCCATTTGTCAGCAGACACGC
# >Rosalind_0808
# CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
# TGGGAACCTGCGGGCAGTAGGTGGAAT

import sys

fastafile = sys.argv[1]

gcdict={}

currentid=None
maxk=None
maxgc=0

with open(fastafile, 'r') as f:
    for l in f:
        l = l.strip()
        if l[0] == '>':
            if currentid:
                if gclen/totlen > maxgc:
                    maxgc = gclen/totlen
                    maxk = currentid
            totlen=0
            gclen=0
            currentid = l[1:]
        else:
            for n in l:
                totlen+=1
                if n in ['C','G']:
                    gclen+=1
# Get last row
if currentid:
    if gclen/totlen > maxgc:
        maxgc = gclen/totlen
        maxk = currentid


print(maxk)
print(maxgc * 100)

if len(sys.argv)>2:
    outfile = sys.argv[2]
    with open(outfile, 'w+') as f:
        f.write(maxk + '\n')
        f.write(str(maxgc * 100))