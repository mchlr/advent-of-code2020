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
        flag = False
        pp = pp.replace("\n", " ") 
        flag = find_and_validate(pp, valid_props)
        if flag: 
            valid_count += 1

    return valid_count


def find_and_validate(ss, props):
    for p in props:
        i = ss.find(p)
        if i != -1:
            switch = {
                # year fields
                "byr:": validate_year(ss[i : i + len(p)], ss[i+ 4 : i + 8]),
                "iyr:": validate_year(ss[i : i + len(p)], ss[ i+ 4 : i + 8]),
                "eyr:": validate_year(ss[i : i + len(p)], ss[i+ 4 : i + 8]),
                # height field
                "hgt:": validate_height(ss[i + len(p) + 3: i + len(p) + 5], ss[i  :  i + 5]),
                # color fields
                "hcl:": validate_color(ss[i : i + len(p)], ss[i + 5 : i + 11]),
                "ecl:": validate_color(ss[i : i + len(p)], ss[i + 5 : i + 7]),
                # pid
                "pid:": validate_pid(ss[i + 4 : i + 13])
            }
            val = switch[p]
            if val:
                debug = "juhu"
            else:
                return False
        else:
            # One property missing => Out
            return False

    return True


def validate_year(k, v):
    try: 
        v = int(v)
    except:
        return False

    switch = {
        "byr:": v >= 1920 and v <= 2002,
        "iyr:": v >= 2010 and v <= 2020,
        "eyr:": v >= 2020 and v <= 2030
    }
    return switch.get(k)


def validate_height(k, v):
    try: 
        v = int(v)
    except:
        return False
        
    switch = {
        "cm": v >= 150 and v <= 193,
        "in": v >= 59 and v <= 76,
    }
    return switch.get(k)


def validate_color(k, v):
    switch = {
        "hcl:": re.match(r"([a-f]|[1-9]){6}", v) != None,
        "ecl:": _contains_range(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"], v) == 1 ,
    }
    val = switch.get(k)
    if(val):
        return True
    return val


def validate_pid(v):
    return re.match(r"(\d\d\d\d\d\d\d\d\d)", v) != None


def _contains_range(lst, string):
    hits  = 0
    for x in lst:
        if string.find(x) != -1: hits += 1
    return hits

def main():
    sol = solve(load_challenge(),   ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"])
    print("Passwords Valid: ", sol)


# Execute
main()