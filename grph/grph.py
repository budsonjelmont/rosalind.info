# Problem

# A graph whose nodes have all been labeled can be 
# represented by an adjacency list, in which each row of 
# the list contains the two node labels corresponding to a 
# unique edge.

# A directed graph (or digraph) is a graph containing 
# directed edges, each of which has an orientation. 
# That is, a directed edge is represented by an arrow 
# instead of a line segment; the starting and ending nodes 
# of an edge form its tail and head, respectively. 
# The directed edge with tail v and head w is represented 
# by (v,w) (but not by (w,v)). A directed loop is a 
# directed edge of the form (v,v).

# For a collection of strings and a positive integer k
# , the overlap graph for the strings is a directed 
# graph Ok in which each string is represented by a node, 
# and string s is connected to string t with a directed 
# edge when there is a length k suffix of s that matches 
# a length k prefix of t, as long as s≠t; 
# we demand s≠t to prevent directed loops in the overlap 
# graph (although directed cycles may be present).

# Given: A collection of DNA strings in FASTA format 
# having total length at most 10 kbp.

# Return: The adjacency list corresponding to O3. 
# You may return edges in any order.
# Sample Dataset

# >Rosalind_0498
# AAATAAA
# >Rosalind_2391
# AAATTTT
# >Rosalind_2323
# TTTTCCC
# >Rosalind_0442
# AAATCCC
# >Rosalind_5013
# GGGTGGG

# Sample Output

# Rosalind_0498 Rosalind_2391
# Rosalind_0498 Rosalind_0442
# Rosalind_2391 Rosalind_2323

from Bio import SeqIO
import sys

overlapthresh = 3

infile = sys.argv[1]

intdct={}

# Read FASTAs
with open(infile) as handle:
    for index, record in enumerate(SeqIO.parse(handle, "fasta")): 
        intdct[record.id] = record.seq

bpindex = {bp:{} for bp in ["A","C","T","G"]}
lenindex = {}
# Iter over all positions in all sequences and build an index of where each base occurs
#   {"A":{id1: [1]}, id2: [2])], "C": {id2: [1]}, "T": {id2: [2]}, "G": {}}
for id, seq in intdct.items():
    lenindex[id] = len(seq)
    for pos, bp in enumerate(seq):
        if id not in bpindex[bp].keys():
            bpindex[bp][id] = [pos]
        else:
            bpindex[bp][id].append(pos)

# Iter over all sequences again and do the following:
overlaps = [] # list of tuples
for id1, seq1 in intdct.items():
    print(id1)
    id1len = lenindex[id1]
    tmpoverlaps = {} # e.g. {"id2":{15:[15], 17: [17]}}
    for pos1, bp1 in enumerate(seq1):
        print(f"{pos1} : {bp1}")
        print(tmpoverlaps)
        nomatchdct = {}
        # Check all the existing matches to see if we can extend
        for id2, matchdct in tmpoverlaps.items():
            print(f"Checking against existing match {id2}")
            id2len = lenindex[id2]
            for matchstartpos, poslst in matchdct.items():
                nextid2pos = (poslst[len(poslst)-1])+1
                if nextid2pos < id2len:
                    if intdct[id2][nextid2pos] == bp1: # Extend the match
                        print(f"Found a match to extend: ({id2}) {matchstartpos} : {nextid2pos}")
                        tmpoverlaps[id2][matchstartpos].append(nextid2pos)
                    else: # No match
                        if id2 not in nomatchdct:
                            nomatchdct[id2] = [matchstartpos]                        
                        else:
                            nomatchdct[id2].append(matchstartpos)
                # Check if the match is complete
                if nextid2pos == (id2len - 1) or pos1 == (id1len - 1):
                    if len(poslst) >= overlapthresh:
                        overlaps.append((id1,id2))
                    else: # No match
                        if id2 not in nomatchdct:
                            nomatchdct[id2] = [matchstartpos]                        
                        else:
                            nomatchdct[id2].append(matchstartpos)
        print("Failed matches:")
        print(nomatchdct)
        for nomatchid2, nomatchstartlst in nomatchdct.items():
            for nomatchstartpos in nomatchstartlst:
                print(f"Terminate match: ({nomatchid2}) {nomatchstartpos}")
                try:
                    tmpoverlaps[nomatchid2].pop(matchstartpos, None)
                except KeyError as e:
                    pass
                try:
                    if not tmpoverlaps[nomatchid2]:
                            tmpoverlaps.pop(nomatchid2, None)
                except KeyError as e:
                    pass
        # For each other seq ID that has an occurrence of the base
        for id2 in [i for i in bpindex[bp1] if i!=id1]:
            # For each position in that ID where the base occurs
            for pos2 in bpindex[bp1][id2]:
                print(f"Initializing new match for {id2} : {pos2}")
                if id2 not in tmpoverlaps.keys():
                    tmpoverlaps[id2] = {pos2:[pos2]}
                else:
                    tmpoverlaps[id2][pos2] = [pos2]

# Return results
print("RESULTS ARE IN")
print(overlaps)
# for i in overlaps:
#     print(f"{i[0]} {i[1]}")