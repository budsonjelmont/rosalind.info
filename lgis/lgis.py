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
 
# reconstruct the longest subsequence
def get_subsequence(seq, tail_ixs, prev_ixs, len):
    i = tail_ixs[len]
    subseq=[]
    while(i >= 0):
        subseq+=[seq[i]]
        i = prev_ixs[i]
    return subseq[::-1]

 # longest increasing subsequence
def lis(arr, n):
    
    # Array where each position's value is the index in arr that marks the tail of a subsequence with length == that position index. Zero-padded.
    tail_ixs =[0 for i in range(n + 1)]  

    # Array where each position's value is the arr index of the predecessor of the longest subsequence ending at that position. Initialized with -1. Zero-padded.
    prev_ixs =[-1 for i in range(n + 1)]  
    
    # Initialized to 1 since there will always be a subsequence of at least this length
    len = 1 
    
    for i in range(1,n):
    
        if arr[i] <= arr[tail_ixs[0]]:
            tail_ixs[0] = tail_ixs[1] = i
        elif arr[i] > arr[tail_ixs[len]]:
            prev_ixs[i] = tail_ixs[len]
            len += 1
            tail_ixs[len] = i
        else:
            # Binary search to find the first tail index >= this element
            l = 0
            r = len
            while l < r:
                pos = (l + r)// 2
                if arr[tail_ixs[pos]] >= arr[i]:
                    r = pos - 1
                elif arr[tail_ixs[pos]] < arr[i]:
                    l = pos + 1
            prev_ixs[i] = tail_ixs[l-1]
            tail_ixs[l] = i

    return get_subsequence(arr, tail_ixs, prev_ixs, len)

# longest decreasing subsequence
def lds(arr, n):

    # Array where each position's value is the index in arr that marks the tail of a subsequence with length == that position index. Zero-padded.
    tail_ixs =[0 for i in range(n + 1)]  

    # Array where each position's value is the arr index of the predecessor of the longest subsequence ending at that position. Initialized with -1. Zero-padded.
    prev_ixs =[-1 for i in range(n + 1)]  
    
    # Initialized to 1 since there will always be a subsequence of at least this length
    len = 1 
    
    for i in range(1,n):
    
        if arr[i] >= arr[tail_ixs[1]]:
            tail_ixs[1] = i
        elif arr[i] < arr[tail_ixs[len]]:
            prev_ixs[i] = tail_ixs[len]
            len += 1
            tail_ixs[len] = i
        else:
            # Binary search to find the first tail index <= this element
            l = 0
            r = len
            while l < r:
                pos = (l + r)// 2
                if arr[tail_ixs[pos]] <= arr[i]:
                    r = pos - 1
                elif arr[tail_ixs[pos]] > arr[i]:
                    l = pos + 1
            prev_ixs[i] = tail_ixs[l-1]
            tail_ixs[l] = i

    return get_subsequence(arr, tail_ixs, prev_ixs, len)

if __name__ == "__main__":
    if len(sys.argv)>1:
        infile = sys.argv[1]
        with open(infile, 'r') as f:
            n = int(f.readline())
            seqstr = f.readline()
            seq = [int(i) for i in seqstr.split()]
    else:
        n=int(input())
        seq=[int(i) for i in input().split()]

    li_subseq = " ".join([str(s) for s in lis(seq, n)])
    ld_subseq = " ".join([str(s) for s in lds(seq, n)])

    print(f'{li_subseq}\n{ld_subseq}')

    if len(sys.argv)>2:
        outfile = sys.argv[2]
        with open(outfile, 'w+') as f:
            f.write(f'{li_subseq}\n{ld_subseq}')