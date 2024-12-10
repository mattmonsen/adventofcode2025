#!/usr/bin/env python3

from collections import deque
import numpy as np

content = open("day_10_input.txt").read()

# Parse the input map into a 2D list
def parse_map(input_str):
    return np.array([[int(char) for char in line.strip()] for line in input_str.strip().split('\n')])

# Find all trailheads (positions with height 0)
def find_trailheads(topographic_map):
    trailheads = []
    rows, cols = topographic_map.shape
    for r in range(rows):
        for c in range(cols):
            if topographic_map[r, c] == 0:
                trailheads.append((r, c))
    return trailheads

# Perform BFS to find all reachable '9's from a trailhead
def bfs_find_nines(topographic_map, start):
    rows, cols = topographic_map.shape
    queue = deque([start])
    visited = set([start])
    reachable_nines = set()

    while queue:
        r, c = queue.popleft()

        # If the current position is a '9', add it to the reachable set
        if topographic_map[r, c] == 9:
            reachable_nines.add((r, c))

        # Check all four possible directions (up, down, left, right)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                # Ensure the path is valid (increasing by exactly 1)
                if topographic_map[nr, nc] == topographic_map[r, c] + 1:
                    visited.add((nr, nc))
                    queue.append((nr, nc))

    return reachable_nines

# Calculate the total score of all trailheads
def calculate_total_score(topographic_map):
    trailheads = find_trailheads(topographic_map)
    total_score = 0

    for trailhead in trailheads:
        reachable_nines = bfs_find_nines(topographic_map, trailhead)
        total_score += len(reachable_nines)

    return total_score

# Example input map as a string (replace this with actual input for testing)
input_map = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

# Parse the input and calculate the total score
topographic_map = parse_map(content)
total_score = calculate_total_score(topographic_map)

print("Total Score:", total_score)

