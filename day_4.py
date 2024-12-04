#!/usr/bin/env python3

import pprint

def load_file_to_2d_array(file_path):
    array = []
    with open(file_path, 'r') as file:
        for line in file:
            array.append(list(line.rstrip()))
    return array

board = load_file_to_2d_array('day_4_input.txt')
#pprint.pprint(board)

def count_pattern_occurrences(board, pattern):
    rows, cols = len(board), len(board[0])
   
    def matches_pattern(r, c):
        for dr in range(3):
            for dc in range(3):
                pr, pc = r + dr, c + dc
                if pr >= rows or pc >= cols:
                    return False
                expected = pattern[dr][dc]
                if expected is not None and board[pr][pc] != expected:
                    return False
        return True

    count = 0
    for r in range(rows - 2):  
        for c in range(cols - 2):
            if matches_pattern(r, c):
                count += 1

    return count

def count_word_occurrences(board, word):
    rows, cols = len(board), len(board[0])
    
    directions = [
        (0, 1),  # Right
        (0, -1),  # Left
        (1, 0),  # Down
        (-1, 0),  # Up
        (-1, -1),  # Top-left
        (-1, 1),  # Top-right
        (1, -1),  # Bottom-left
        (1, 1)  # Bottom-right
    ]
    
    def dfs(i, j, direction, k):

        if k == len(word):
            return 1

        if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[k]:
            return 0
       
        count = dfs(i + direction[0], j + direction[1], direction, k + 1)
        
        return count
    
    total_count = 0
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == word[0]: 
                for direction in directions: 
                    total_count += dfs(row + direction[0], col + direction[1], direction, 1)
    
    return total_count

patterns = [
[
    ('M', None, 'M'),
    (None, 'A', None),
    ('S', None, 'S')
],
[
    ('M', None, 'S'),
    (None, 'A', None),
    ('M', None, 'S')
],
[
    ('S', None, 'M'),
    (None, 'A', None),
    ('S', None, 'M')
],
[
    ('S', None, 'S'), 
    (None, 'A', None),
    ('M', None, 'M')
]
]

total_xmas = 0

for pattern in patterns:
    total_xmas += count_pattern_occurrences(board, pattern)

print(f"Total pattern occurrences: {total_xmas}")

print(count_word_occurrences(board, "XMAS"))
