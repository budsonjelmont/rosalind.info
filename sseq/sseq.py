import sys
from Bio import SeqIO

infile = sys.argv[1]

dnas=None
motif=None

with open(infile) as handle:
    for index, record in enumerate(SeqIO.parse(handle, "fasta")): 
        if index == 0:
            dnas = record.seq
        elif index == 1:
            motif = record.seq
        else:
            print("Too many sequences in FASTA file!")
            sys.exit()

# dnas='TAGTAAAAG'
# motif='AAAG'

nucposix = {n:[] for n in ['A','T','C','G']}

for pos in range(0,len(dnas)):
    nucposix[dnas[pos]].append(pos)

path = []
for motifnuc in motif: # each position in motif
    for nucix in nucposix[motifnuc]: # each letter occurrence 
        if not path:
            path.append(nucix)
            break
        else:
            if nucix > path[len(path)-1]: # If current index > last index
                path.append(nucix)     
                break

motifinst1 = ' '.join([str(i+1) for i in path])

# instancedct = {n:[] for n in ['A','T','C','G','complete']}
# instancedct[motif[0]].append([])
# for ix in range(0,len(dnas)):
#     nuc = dnas[ix] # Nuc at current position
#     extensions = {n:[] for n in instancedct.keys()}
#     # Check existing instances
#     for instance in instancedct[nuc]:
#         nextix = len(instance)+1
#         if nextix < len(motif):
#             nextnuc = motif[nextix]
#             extensions[nextnuc].append(instance + [ix])
#         else:
#             instancedct['complete'].append(instance + [ix])
#     # Initialize a new motif instance
#     for k,v in extensions.items():
#         for arr in v:
#             instancedct[k].append(arr)

# motifinst1 = ' '.join([str(i) for i in instancedct['complete'][0]])

print(motifinst1)

if len(sys.argv)>2:
    outfile = sys.argv[2]
    with open(outfile, 'w+') as f:
        f.write(motifinst1)