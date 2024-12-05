#!/usr/bin/env python3
    
rules = open("day_5_rules.txt").read()
prints = open("day_5_print.txt").read()

#rules = open("rule.txt").read()
#prints = open("print.txt").read()

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
                return False

    return False

def reorder_print(line):
    while(not check_rule(line)):
        for i in range(len(line) - 2, -1, -1):
            if not check_rule(line[i:]):
                a = line[i]
                b = line[i + 1]
                line[i] = b
                line[i + 1] = a

    return line

pages = 0
reorder_sum = 0

for line in prints.splitlines():
    new_print = line.split(",")
    if check_rule(new_print):
        length= len(new_print)
        if length % 2 != 0:
            middle = length // 2
            pages += int(new_print[middle])
    else:
        reordered = reorder_print(new_print)
        length = len(reordered)
        if length % 2 != 0:
            middle = length // 2
            reorder_sum += int(reordered[middle])

print(pages)
print(reorder_sum)
