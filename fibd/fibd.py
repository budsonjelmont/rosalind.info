# Problem
# Figure 4. A figure illustrating the propagation of Fibonacci's rabbits if they die after three months.

# Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2
# and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.
# Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

# Given: Positive integers n≤100
# and m≤20

# Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m
# months.
# Sample Dataset

# 6 3

# Sample Output

# 4

import sys

mos = int(sys.argv[1])
live = int(sys.argv[2])

# mos = 6
# live = 3

bunlist = [0 for l in range(0,live)]
bunlist[0] = 1
for m in range(0+1, mos):
    print('month: ' + str(m))
    print('number of buns: ' + str(sum(bunlist)))
    newbuns = 0
    for l in range(live-1,0-1,-1):
        print(str(bunlist[l]) + ' buns that are ' + str(l) + ' mos old')
        if l+1 != live:
            bunlist[l+1] = bunlist[l]
        if l != 0:
            newbuns+= bunlist[l]
    bunlist[0] = newbuns

print(bunlist)
print('total buns: ' + str(sum(bunlist)))