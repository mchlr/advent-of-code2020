import os
import math
import re


def load_challenge():
    p = os.path.join(os.path.dirname(__file__), 'challenge.txt')
    cont = open(p)
    return list(cont.read().split("\n\n"))
    

def solve(lst, valid_props):
    valid_count = 0
    for pp in lst:
        flag = True
        pp = pp.replace("\n", " ")
        for vp in valid_props:
            if(pp.find(vp) == -1):
                flag = False
                break    
        if flag: valid_count += 1
            
    return valid_count


def main():
    sol = solve(load_challenge(),   ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    print("Passwords Valid: ", sol)


# Execute
main()