import sys
from Bio import SeqIO

infile = sys.argv[1]

seqs=[]

with open(infile) as handle:
    for index, record in enumerate(SeqIO.parse(handle, "fasta")): 
        seqs.append(record.seq)

nucposcount = {n:[0 for i in range(0,len(seqs[0]))] for n in ['A','T','C','G']}
conseq = ''

for i in range(0,len(seqs[0])):
    maxcountnuc=None
    maxcount=0
    for seq in seqs:
        nuc = seq[i]
        nucposcount[nuc][i]+=1
        if nucposcount[nuc][i] > maxcount:
            maxcount = nucposcount[nuc][i]
            maxcountnuc = nuc
    conseq += maxcountnuc

print(conseq)
for k,v in nucposcount.items():
    print(k + ': ' + ' '.join([str(n) for n in v]))

if len(sys.argv)>2:
    outfile = sys.argv[2]
    with open(outfile, 'w+') as f:
        f.write(conseq + '\n')
        for k,v in nucposcount.items():
            f.write(k + ': ' + ' '.join([str(n) for n in v]) + '\n')
