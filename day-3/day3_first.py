import os
import math
import re


def load_challenge():
    p = os.path.join(os.path.dirname(__file__), 'challenge.txt')
    cont = open(p)
    return list(cont.read().split("\n"))
    
def solve(map):
    tree_count = 0
    xindex = 0
    for line in map:
        arr = list(line)
        if(arr[(xindex % len(arr))] == "#"):
            tree_count += 1
        xindex += 3

    return tree_count 

def main():
    sol = solve(load_challenge())
    print("Trees hit: ", sol)


# Execute
main()