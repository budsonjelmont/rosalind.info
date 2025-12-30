# Problem
# A subsequence of a permutation is a collection of elements of the permutation in the order that they appear. For example, (5, 3, 4) is a subsequence of (5, 1, 3, 4, 2).
# A subsequence is increasing if the elements of the subsequence increase, and decreasing if the elements decrease. For example, given the permutation (8, 2, 1, 6, 5, 7, 4, 3, 9), an increasing subsequence is (2, 6, 7, 9), and a decreasing subsequence is (8, 6, 5, 4, 3). You may verify that these two subsequences are as long as possible.

# Given: A positive integer n≤10000
#  followed by a permutation π
#  of length n.

# Return: A longest increasing subsequence of π, 
# followed by a longest decreasing subsequence of π.

# Sample Dataset
# 5
# 5 1 4 2 3
# Sample Output
# 1 2 3
# 5 4 2

import sys

n=input()
seq=[int(i) for i in input().split()]

def calc_mtx(seq, asc=True): 
    running_totals = []
    mtx = [[{'op':'-','score':0,'last_ix':()} for s in seq] for s in seq]
    for j in range(0,len(seq)): # column-major
        # initialize column max variables to track the longest subsequence that terminates in this column
        running_total = 0
        running_total_ix = (-1,-1)
        for i in range(0,len(seq)):
            if i > j:
                continue
            elif i == j:
                mtx[i][j] = {'op':'o','score':1, 'last_ix':()} # start a new subsequence
            else:
                if (asc and seq[j] > seq[i]) or (not asc and seq[j] < seq[i]):
                    mtx[i][j] = {'op':'e','score':running_totals[i]['total']+1,'last_ix':(running_totals[i]['total_ix'])}
                else:
                    mtx[i][j] = {'op':None,'score':None,'last_ix':None}
            # calculate the highest scoring subsequence at this position
            if (0 if mtx[i][j]['score'] is None else mtx[i][j]['score']) > running_total:
                running_total = mtx[i][j]['score']
                running_total_ix = (i,j)
        running_totals += [{'total':running_total, 'total_ix':running_total_ix}]
    return {'matrix':mtx,'column_maxes':running_totals}

def get_subsequence(subseq, ix, seq, mtx):
    current = mtx[ix[0]][ix[1]]
    subseq += [seq[ix[1]]]
    if current['op']=='e':
        next_ix = current['last_ix']
        return get_subsequence(subseq, next_ix, seq, mtx)
    elif current['op']=='o':
        return subseq

asc_result = calc_mtx(seq)
asc_mtx = asc_result['matrix']
asc_running_totals = asc_result['column_maxes']

asc_max_of_totals = 0
asc_max_of_totals_ix = (0,0)

for running_total in asc_running_totals:
    if running_total['total'] > asc_max_of_totals:
        asc_max_of_totals = running_total['total']
        asc_max_of_totals_ix = running_total['total_ix']

asc_subseq = get_subsequence([], asc_max_of_totals_ix, seq, asc_mtx)
asc_subseq_str = " ".join([str(i) for i in asc_subseq[::-1]]) # array elements are in reverse order

dsc_result = calc_mtx(seq, asc=False)
dsc_mtx = dsc_result['matrix']
dsc_running_totals = dsc_result['column_maxes']

dsc_max_of_totals = 0
dsc_max_of_totals_ix = (0,0)

for running_total in dsc_running_totals:
    if running_total['total'] > dsc_max_of_totals:
        dsc_max_of_totals = running_total['total']
        dsc_max_of_totals_ix = running_total['total_ix']

dsc_subseq = get_subsequence([], dsc_max_of_totals_ix, seq, dsc_mtx)
dsc_subseq_str = " ".join([str(i) for i in dsc_subseq[::-1]]) # array elements are in reverse order

print(asc_subseq_str)
print(dsc_subseq_str)

if len(sys.argv)>1:
    outfile = sys.argv[1]
    with open(outfile, 'w+') as f:
        f.write(f'{asc_subseq_str}\n{dsc_subseq_str}')