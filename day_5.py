#!/usr/bin/env python3

#rules = open("day_5_rules.txt").read()
#prints = open("day_5_print.txt").read()

rules = open("rule.txt").read()
prints = open("print.txt").read()

dictionary = {}

for rule in rules.splitlines():
    a, b = rule.split("|")
    if a in dictionary.keys():
        dictionary[a][b] = True 
    else:
        dictionary[a] = {}
        dictionary[a][b] = True

def check_rule(line):
    if len(line) == 1:
        return True

    first = line[0]
    if first in dictionary:
        for i in range(1, len(line)):
            check = line[i]
            if check in dictionary[first]:
                return check_rule(line[1:])
            else:
#                print("didn't find a matching rule")
                return False
#    else:
#        print(f"dictionary check failed on key {first}")

#    print("got to end")
    return False

pages = 0

for line in prints.splitlines():
    new_print = line.split(",")
    if check_rule(new_print):
        length= len(new_print)
        if length % 2 != 0:
            middle = length // 2
            pages += int(new_print[middle])

print(pages)
