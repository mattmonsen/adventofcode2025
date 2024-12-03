#!/usr/bin/env python3

import re

with open('day_3_input.txt', 'r') as f:
    contents = f.read()

result = re.findall("mul\((\d+),(\d+)\)", contents)
print(result)

total = 0

for match in re.finditer("mul\((\d+),(\d+)\)", contents):
    total += int(match.group(1)) * int(match.group(2))

print(total)
