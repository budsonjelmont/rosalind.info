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

def recur_count_perm(n):
    if n == 1:
        return 1
    else:
        return n * recur_count_perm(n-1)

def recur_build_tree(perm, nums_left):
    if len(nums_left) == 1:
        return nums_left[0]
    else:
        for n1 in nums_left:
            perm[n1] = recur_build_tree({}, [n2 for n2 in nums_left if n2!= n1])
        return perm

def recur_write_nodes_to_file(node,nodelist,f):
    if not isinstance(node, dict):
        nodelist.append(node)
        print(' '.join([str(n1) for n1 in nodelist]))
        f.write(' '.join([str(n1) for n1 in nodelist]) + '\n')
    else:
        for k,v in node.items():
            recur_write_nodes_to_file(v, nodelist + [k],f)

n = int(sys.argv[1])

#n = 6
 
t = recur_build_tree({}, list(range(1,n+1)))

if len(sys.argv)>2:
    outfile = sys.argv[2]
    with open(outfile, 'w+') as f:
        f.write(str(recur_count_perm(n)) + '\n')
        recur_write_nodes_to_file(t,[],f)
