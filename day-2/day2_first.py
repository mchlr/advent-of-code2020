import os
import math

valid_count = 0

def load_challenge():
    p = os.path.join(os.path.dirname(__file__), 'challenge.txt')
    cont = open(p)
    return list(cont.read().split("\n"))
    
def solve(pws):
    for pw in pws:
        # do stuff here
        return 0

def main():
    solve(load_challenge())
    print("Passwords Valid: ", valid_count)


# Execute
main()