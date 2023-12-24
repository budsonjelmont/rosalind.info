# Problem
# Figure 2. The probability of any outcome (leaf) in a probability tree diagram is given by the product of probabilities from the start of the tree to the outcome. For example, the probability that X is blue and Y is blue is equal to (2/5)(1/4), or 1/10.

# Probability is the mathematical study of randomly occurring phenomena. We will model such a phenomenon with a random variable, which is simply a variable that can take a number of different distinct outcomes depending on the result of an underlying random process.

# For example, say that we have a bag containing 3 red balls and 2 blue balls. If we let X
# represent the random variable corresponding to the color of a drawn ball, then the probability of each of the two outcomes is given by Pr(X=red)=35 and Pr(X=blue)=25.

# Random variables can be combined to yield new random variables. Returning to the ball example, let Y
# model the color of a second ball drawn from the bag (without replacing the first ball). The probability of Y being red depends on whether the first ball was red or blue. To represent all outcomes of X and Y, we therefore use a probability tree diagram. This branching diagram represents all possible individual probabilities for X and Y, with outcomes at the endpoints ("leaves") of the tree. The probability of any outcome is given by the product of probabilities along the path from the beginning of the tree; see Figure 2 for an illustrative example.

# An event is simply a collection of outcomes. Because outcomes are distinct, the probability of an event can be written as the sum of the probabilities of its constituent outcomes. For our colored ball example, let A
# be the event "Y is blue." Pr(A) is equal to the sum of the probabilities of two different outcomes: Pr(X=blue and Y=blue)+Pr(X=red and Y=blue), or 310+110=25

# (see Figure 2 above).

# Given: Three positive integers k
# , m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n
# are homozygous recessive.

# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
# Sample Dataset

# 2 2 2

# Sample Output

# 0.78333

import sys

from itertools import accumulate
from functools import reduce
from operator import mul, add

infile = sys.argv[1]

with open(infile, 'r') as f:
    k,m,n = f.readline().strip().split(' ')

# k=1 # A/A
# m=1 # A/a
# n=1 # a/a

def recur_build_tree(partners,homdom,het,homrec,t):
    if partners>1:
        return {'homdom':{},'het':{},'homrec':{}}
    else:
        for z in ['homdom','het','homrec']:
            if z == 'homdom':
                t[z] = {'p':homdom/(homdom + het + homrec), 't':recur_build_tree(partners+1, max(homdom-1,0), het, homrec, {})}
            elif z == 'het':
                t[z] = {'p':het/(homdom + het + homrec),'t':recur_build_tree(partners+1, homdom, max(het-1,0), homrec, {})}
            elif z == 'homrec':
                t[z] = {'p':homrec/(homdom + het + homrec), 't':recur_build_tree(partners+1, homdom, het, max(homrec-1,0), {})}
        return t

def recur_get_prob(t,zlst,plst):
    if not t['homdom']:
        if set(zlst) == set(['homdom']):
            plst.append(1)
        elif set(zlst) == set(['het']):
            plst.append(0.75)
        elif set(zlst) == set(['homrec']):
            plst.append(0)
        elif set(zlst) == set(['homdom','het']):
            plst.append(1)
        elif set(zlst) == set(['homdom','homrec']):
            plst.append(1)
        elif set(zlst) == set(['het','homrec']):
            plst.append(0.5)
        cumplst.append(reduce(mul,plst,1))
    else:
        for z in t.keys():
            recur_get_prob(t[z]['t'],zlst + [z],plst + [t[z]['p']])

tree = recur_build_tree(0,int(k),int(m),int(n),{})
cumplst = []
recur_get_prob(tree, [], [])

prob = reduce(add,cumplst,0)

if len(sys.argv)>2:
    outfile = sys.argv[2]
    with open(outfile, 'w+') as f:
        f.write(str(prob))