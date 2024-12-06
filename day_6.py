#!/usr/bin/env python3

import pprint

turns = 0

def load_file_to_2d_array(file_path):
    array = []
    with open(file_path, 'r') as file:
        for line in file:
            array.append(list(line.rstrip()))
    return array

board = load_file_to_2d_array('day_6_input.txt')
#pprint.pprint(board)


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

def on_board(x,y):
    if x < 0 or y < 0 or x >= len(board) or y >= len(board):
        return False
    else:
        return True

def locate_guard():
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] in directions.keys():
                return x, y
    return -1, -1

def lookahead_safe(x, y):
    if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] == "#":
        return False 
    return True

def turn():
    x, y = locate_guard()
    board[x][y] = turn_dir[board[x][y]]

def move():
    x, y = locate_guard();
    dir_x, dir_y = directions[board[x][y]]
    if lookahead_safe(x + dir_x, y + dir_y):
        board[x + dir_x][y + dir_y] = board[x][y]
        board[x][y] = "X"
    elif not on_board(x + dir_x, y + dir_y):
        board[x][y] = "X"
        return False
    else:
        global turns
        turns += 1
        turn()
        
    return True

def count():
    count = 0
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == "X":
                count += 1
    return count

counter = 0
while(move()):
    counter += 1

print(count())
print(turns)
