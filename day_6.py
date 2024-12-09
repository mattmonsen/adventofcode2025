#!/usr/bin/env python3

import pprint
import copy

def load_file_to_2d_array(file_path):
    array = []
    with open(file_path, 'r') as file:
        for line in file:
            array.append(list(line.rstrip()))
    return array

orig_board = load_file_to_2d_array('day_6_input.txt')
board = copy.deepcopy(orig_board)

directions = {
    "^": [-1,0],
    ">": [0,1],
    "v": [1,0],
    "<": [0,-1]
}

turn_dir = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^"
}

def is_board_loop(board):
    visited_states = set()

    def on_board(x,y):
        if x < 0 or y < 0 or x >= len(board) or y >= len(board):
            return False
        else:
            return True

    def locate_guard():
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] in directions.keys():
                    return x, y, board[x][y]
        return -1, -1

    def lookahead_safe(x, y):
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] == "#":
            return False 
        return True
    
    def turn():
        x, y, direction = locate_guard()
        board[x][y] = turn_dir[board[x][y]]
    
    def move():
        x, y, direction = locate_guard();
        state = (x, y, direction)
        if state in visited_states:
            print(state)
            return False
        dir_x, dir_y = directions[board[x][y]]
        if lookahead_safe(x + dir_x, y + dir_y):
            board[x + dir_x][y + dir_y] = board[x][y]
            board[x][y] = "."
            visited_states.add(state)
        elif not on_board(x + dir_x, y + dir_y):
            return False
        else:
            turn()
            
        return True
    
    counter = 0
    while(move()):
        counter += 1
    x, y, direction = locate_guard()
    dir_x, dir_y = directions[board[x][y]]
    if on_board(x + dir_x, y + dir_y):
        return True
    return False

counter = 0
for x in range(len(board)):
    for y in range(len(board[0])):
        print(f"Running: ({x}, {y})")
        if board[x][y] == '.':
            board[x][y] = "#"
            if is_board_loop(board):
                print(counter)
                counter += 1
            board = copy.deepcopy(orig_board) 

print(counter)
