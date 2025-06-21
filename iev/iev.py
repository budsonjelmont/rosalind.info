# Problem

# For a random variable X taking integer values between 1 and n, the expected value of X is E(X)=∑nk=1k×Pr(X=k).
# The expected value offers us a way of taking the long-term average of a random variable over a large number of trials.

# As a motivating example, let X
# be the number on a six-sided die. Over a large number of rolls, we should expect to obtain an average of 3.5 on the die
# (even though it's not possible to roll a 3.5). The formula for expected value confirms that E(X)=∑6k=1k×Pr(X=k)=3.5.

# More generally, a random variable for which every one of a number of equally spaced outcomes has the same probability is called
# a uniform random variable (in the die example, this "equal spacing" is equal to 1). We can generalize our die example to find that if X
# is a uniform random variable with minimum possible value a and maximum possible value b, then E(X)=(a+b)/2. You may also wish to verify that
# for the dice example, if Y is the random variable associated with the outcome of a second die roll, then E(X+Y)=7.

# Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing
# each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:

#     AA-AA
#     AA-Aa
#     AA-aa
#     Aa-Aa
#     Aa-aa
#     aa-aa

# Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.
# Sample Dataset

# 1 0 0 1 0 1

# Sample Output

# 3.5

import sys

AAAA = int(sys.argv[1])
AAAa = int(sys.argv[2])
AAaa = int(sys.argv[3])
AaAa = int(sys.argv[4])
Aaaa = int(sys.argv[5])
aaaa = int(sys.argv[6])

genotypes = {
    "AAAA": {"geno1": "AA", "geno2": "AA", "n": AAAA},
    "AAAa": {"geno1": "AA", "geno2": "Aa", "n": AAAa},
    "AAaa": {"geno1": "AA", "geno2": "aa", "n": AAaa},
    "AaAa": {"geno1": "Aa", "geno2": "Aa", "n": AaAa},
    "Aaaa": {"geno1": "Aa", "geno2": "aa", "n": Aaaa},
    "aaaa": {"geno1": "aa", "geno2": "aa", "n": aaaa},
}


def prob_of_dominant_pheno(geno1, geno2):
    genos = []
    for g1 in geno1:
        for g2 in geno2:
            genos.append((g1, g2))
    return len([g for g in genos if "A" in g]) / len(genos)


def prob_of_recessive_pheno(geno1, geno2):
    return 1 - prob_of_dominant_pheno(geno1, geno2)


def expected_value(p0, p1, p2):
    return (0 * p0) + (p1) + (2 * p2)


result = 0
for k, v in genotypes.items():
    result += v["n"] * expected_value(
        prob_of_recessive_pheno(v["geno1"], v["geno2"]) ** 2,
        2
        * prob_of_dominant_pheno(v["geno1"], v["geno2"])
        * prob_of_recessive_pheno(v["geno1"], v["geno2"]),
        prob_of_dominant_pheno(v["geno1"], v["geno2"]) ** 2,
    )

print(result)
