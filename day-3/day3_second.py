import os
import math
import re


def load_challenge():
    p = os.path.join(os.path.dirname(__file__), 'challenge.txt')
    cont = open(p)
    return list(cont.read().split("\n"))
    
def solve(map, x_add, y_add):
    tree_count = 0
    xindex = 0
    yindex = 0
    while True:
        arr = list(map[yindex])
        if(arr[(xindex % len(arr))] == "#"):
            tree_count += 1
        xindex += x_add
        yindex += y_add
        if(yindex >= len(map)):
            break

    return tree_count 

def main():
    # 1,1
    sol_a = solve(load_challenge(), 1, 1)
    # 3,1
    sol_b = solve(load_challenge(), 3, 1)
    # 5,1
    sol_c = solve(load_challenge(), 5, 1)
    # 7,1
    sol_d = solve(load_challenge(), 7, 1)
    # 1,2
    sol_e = solve(load_challenge(), 1, 2)

    print("1,1: ", sol_a)
    print("3,1: ", sol_b)
    print("5,1: ", sol_c)
    print("7,1: ", sol_d)
    print("1,2: ", sol_e)
    print("=> ", (sol_a * sol_b * sol_c * sol_d * sol_e))


# Execute
main()