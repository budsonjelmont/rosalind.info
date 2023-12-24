# Problem

# A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.

# Given: A positive integer n≤7

# Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

# Sample Dataset

# 3

# Sample Output

# 6
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1

import sys

plst = []
def recur_perm(l, nums_left):
    if len(nums_left) == 1:
        plst.append(l + [nums_left[0]])
    else:
        for n1 in nums_left:
            recur_perm(l + [n1], [n2 for n2 in nums_left if n2!= n1])

n = int(sys.argv[1])

#n = 6
 
recur_perm([], list(range(1,n+1)))

if len(sys.argv)>2:
    outfile = sys.argv[2]
    with open(outfile, 'w+') as f:
        f.write(str(len(plst)) + '\n')
        for p in plst:
            f.write(' '.join([str(p1) for p1 in p]) + '\n')
