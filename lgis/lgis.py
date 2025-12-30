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

n=input()
seq=[int(i) for i in input().split()]

def get_subsequence(subseq, ix, seq, mtx):
    current = mtx[ix[0]][ix[1]]
    subseq += [seq[ix[1]]]
    if current['op']=='e':
        next_ix = current['last_ix']
        return get_subsequence(subseq, next_ix, seq, mtx)
    elif current['op']=='o':
        return subseq

asc_mtx = dsc_mtx = [[{'op':'-','score':0,'last_ix':()} for s in seq] for s in seq]
colmaxes = []

for j in range(0,len(seq)): # column-major
    # initialize column max variables to track the longest subsequence that terminates in this column
    colmax = 0
    colmax_ix = (-1,-1)
    for i in range(0,len(seq)):
        if i > j:
            continue
        elif i == j:
            asc_mtx[i][j] = {'op':'o','score':1, 'last_ix':()} # start a new subsequence
        else:
            if seq[j] < seq[i]: # previous 
                asc_mtx[i][j] = {'op':'e','score':colmaxes[i][0]+1,'last_ix':(colmaxes[i][1])}
            else:
                asc_mtx[i][j] = {'op':None,'score':None,'last_ix':None}
        # calculate the highest scoring subsequence at this position
        if (0 if asc_mtx[i][j]['score'] is None else asc_mtx[i][j]['score']) > colmax:
            colmax = asc_mtx[i][j]['score']
            colmax_ix = (i,j)
    colmaxes += [(colmax, colmax_ix)]

max_of_maxes = 0
max_of_maxes_ix = (0,0)

for colmax in colmaxes:
    if colmax[0] > max_of_maxes:
        max_of_maxes = colmax[0]
        max_of_maxes_ix = colmax[1]

subseq = get_subsequence([], max_of_maxes_ix, seq, asc_mtx)
print(" ".join([str(i) for i in subseq[::-1]]))