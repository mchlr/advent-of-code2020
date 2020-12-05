import os
import json
import math

def load_challenge():
    p = os.path.join(os.path.dirname(__file__), 'challenge.json')
    file = open(p)
    return json.load(file)

def solve(lst):
    lst = sorted(lst)
    for idx, curr in enumerate(lst):
        print("---------- NEW CURRENT (", curr ,") ----------")#
        if((idx + 1) != len(lst)):
            iter = doStep(curr, -1, lst)
            if(iter == -1):
                continue
            else:
                return iter
        else:
            return "Fail!"

def doStep(el0, el1, lst):
    if(len(lst) > 0):
        if(el1 == -1):
            splt_idx = math.floor(len(lst) / 2)
            el1 = lst[splt_idx]

        else:
            splt_idx = math.floor(len(lst) / 2)
            el = lst[splt_idx]
            print(el0, " + ", el1, " + ", el, " = ", el0+el1+el)
            if(el0+el1+el > 2020):
                return doStep(el0, el1, lst[0 : splt_idx])
            elif(el0+el1+el < 2020):
                return doStep(el0, el1, lst[splt_idx : len(lst) - 1])
            else:
                return [el0, el1, el]

        if(el0+el1 > 2020):
            return doStep(el0, -1, lst[0 : splt_idx - 1])
        else: # < 2020
            splt_idx = math.floor(len(lst) / 2)
            el = lst[splt_idx]
            t = el0+el1+el
            print(el0, " + ", el1, " + ", el, " = ", t)
            if(t > 2020):
                doStep(el0, el1, lst[0: splt_idx - 1])
            elif(t < 2020):
                doStep(el0, el1, lst[splt_idx:len(lst) - 1])

            return doStep(el0, el1, lst)


        t = el + lst[splt_idx]
        print(el0, " +  ", el1, " + ", lst[splt_idx], " = ", t) # Print a debug message
        if(t > 2020):
            return doStep(el0, el1, lst[0 : splt_idx])
        elif(t < 2020):
            return doStep(el0, el1, lst[splt_idx : len(lst)-1])
        else:
            return [el0, el1, lst[splt_idx]]
    else:
        return -1

def main():
    print("Starting")
    sol = solve(load_challenge())
    print("=> Solved Day 1: ", sol)


main()