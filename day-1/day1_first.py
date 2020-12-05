
# Solves the first challenge from day 1: 
# Find 2 numbers that sum up to 2020.

import os
import json
import math

def load_challenge():
    p = os.path.join(os.path.dirname(__file__), 'challenge.json')
    file = open(p)
    return json.load(file)

def solve(lst):
    lst = sorted(lst)
    for curr in lst:
        # print("---------- NEW CURRENT ----------")
        iter = doStep(curr, lst)
        if(iter == -1):
            continue
        else:
            return iter

def doStep(curr, lst):
    if(len(lst) > 0):
        splt_idx = math.floor(len(lst) / 2) 
        t = curr + lst[splt_idx]
        # print(curr, " + ", lst[splt_idx], " = ", t) Print a debug message
        if(t > 2020):
            return doStep(curr, lst[0 : splt_idx])
        elif(t < 2020):
            return doStep(curr, lst[splt_idx : len(lst)-1])
        else:
            return curr * lst[splt_idx]
    else:
        return -1

def main():
    print("Starting")
    sol = solve(load_challenge())
    print("=> Solved Day 1: ", sol)


main()