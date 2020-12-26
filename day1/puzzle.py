from itertools import combinations
from math import prod

with open("input", "r") as f:
    input = [int(x.strip()) for x in f.readlines()]

def main(n):
    for c in combinations(input, n):
        if sum(c) == 2020:
            print(prod(c))


main(2)
main(3)


