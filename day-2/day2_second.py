import os
import math
import re


def load_challenge():
    p = os.path.join(os.path.dirname(__file__), 'challenge.txt')
    cont = open(p)
    return list(cont.read().split("\n"))
    
def solve(pws):
    valid_count = 0
    for pw in pws:
        matches = re.split(r"(\d*-\d*).(\w): (\w*)", pw)
        # Process the min/max group
        tmp = matches[1].split("-")

        if(verify_password(tmp[0], tmp[1], matches[2], matches[3])):
            valid_count += 1
            
    return valid_count

def verify_password(pos0, pos1, char, pw):
    flag = False
    if(pw[int(pos0) - 1] == char):
        flag = True
    if(pw[int(pos1) - 1] == char):
        flag = not flag

    return flag


def main():
    sol = solve(load_challenge())
    print("Passwords Valid: ", sol)


# Execute
main()