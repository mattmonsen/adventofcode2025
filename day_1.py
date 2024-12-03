#!/usr/bin/env python3

list_1 = []
list_2 = []
distance = 0
similarity = 0

with open('day_1_input.txt', 'r') as f:
    contents = f.read()

lines = contents.splitlines()

for line in lines:
    t = line.split()
    list_1.append(t[0])
    list_2.append(t[1])

list_1.sort()
list_2.sort()

for i in range(len(list_1)):
#    print(i, list_1[i], list_2[i])
    distance += abs(int(list_1[i]) - int(list_2[i]))
    similarity += int(list_1[i]) * list_2.count(list_1[i])

print(distance)
print(similarity)
