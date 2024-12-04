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
    
    # DFS helper function to count occurrences in a given direction
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

print(count_word_occurrences(board, "XMAS"))
