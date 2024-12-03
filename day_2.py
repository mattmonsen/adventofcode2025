#!/usr/bin/env python3

def safe_count(lst):
    increasing = True
    first = True
    for i in range(1, len(lst)):
        if first and int(lst[i]) >= int(lst[i - 1]):
            increasing = False
        first = False
        if increasing and int(lst[i]) >= int(lst[i - 1]):
            return False
        elif not(increasing) and int(lst[i]) <= int(lst[i - 1]):
            return False 
        elif abs(int(lst[i]) - int(lst[i - 1])) > 3:
            return False
    return True

def safe(numbers):
    safe = True
    if safe_count(numbers):
        return True
    else:
        for i in range(len(numbers)):
            new_numbers = numbers.copy()
            del new_numbers[i]
            if safe_count(new_numbers):
                return True
    return False

with open('day_2_input.txt', 'r') as f:
#with open('test.txt', 'r') as f:
    contents = f.read()

lines = contents.splitlines()
count = 0

for line in lines:
    if safe(line.split()):
        count += 1
    
print(count)
