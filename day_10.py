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

# Function to calculate trail ratings using DFS with memoization
def dfs_count_trails(topographic_map, position, memo):
    rows, cols = topographic_map.shape
    r, c = position

    # If this position is already computed, return its value
    if position in memo:
        return memo[position]

    # If this position is height 9, it's a valid endpoint
    if topographic_map[r, c] == 9:
        return 1

    # Count distinct trails from this position
    trails = 0
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            # Ensure the path is valid (increasing by exactly 1)
            if topographic_map[nr, nc] == topographic_map[r, c] + 1:
                trails += dfs_count_trails(topographic_map, (nr, nc), memo)

    # Store the result in memoization table
    memo[position] = trails
    return trails

# Calculate the total ratings of all trailheads
def calculate_total_ratings(topographic_map):
    trailheads = find_trailheads(topographic_map)
    total_ratings = 0
    memo = {}

    for trailhead in trailheads:
        total_ratings += dfs_count_trails(topographic_map, trailhead, memo)

    return total_ratings

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

# Parse the input and calculate the total ratings
topographic_map = parse_map(content)
total_ratings = calculate_total_ratings(topographic_map)

print("Total Ratings:", total_ratings)

