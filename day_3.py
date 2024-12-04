#!/usr/bin/env python3

import re

first_capture = r"^(.*?)don\'t\(\)"
middle_capture = r"do\(\)(.*)don\'t\(\)"
last_capture = r"do\(.*?\)(?!.*do\(.*?\))(.*)$"
extract_capture = r"mul\((\d+),(\d+)\)"
full_capture = r"(?:^|do\(\))(.*?)(?=don't\(\)|$)"
pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"

matches = re.findall(pattern, open("day_3_input.txt").read())

total = 0
flag = True
for match in matches:
    if match == "do()":
        flag = True 
    elif match == "don't()":
        flag = False
    else:
        if flag:
            x, y = map(int, match[4:-1].split(","))
            total += x * y
print(total)
