#!/usr/bin/env python3

def load_file_to_2d_array(file_path):
    array = [] 
    with open(file_path, 'r') as file:
        for line in file:
            array.append(list(line.rstrip()))
    return array    
                
grid = load_file_to_2d_array('day_8_input.txt')

def parse_input(grid):
    """
    Parse the input grid into a dictionary mapping each frequency
    to a list of its antenna positions.
    """
    antennas = {}
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell != '.':
                if cell not in antennas:
                    antennas[cell] = []
                antennas[cell].append((x, y))
    return antennas

def add_antinodes(positions, grid_width, grid_height):
    """
    Calculate all antinode positions for a given set of antennas.
    Includes antennas themselves if aligned with others.
    """
    antinodes = set()
    n = len(positions)
    
    # Compare each pair of antennas
    for i in range(n):
        x1, y1 = positions[i]
        for j in range(n):
            if i == j:
                continue
            x2, y2 = positions[j]
            
            # Include the antennas themselves
            antinodes.add((x1, y1))
            antinodes.add((x2, y2))
            
            # Determine the direction vector (dx, dy)
            dx, dy = x2 - x1, y2 - y1
            
            # Extend antinodes along the line in both directions
            k = 1
            while True:  # Forward extension
                extended = (x2 + k * dx, y2 + k * dy)
                if 0 <= extended[0] < grid_width and 0 <= extended[1] < grid_height:
                    antinodes.add(extended)
                else:
                    break
                k += 1
            
            k = 1
            while True:  # Backward extension
                extended = (x1 - k * dx, y1 - k * dy)
                if 0 <= extended[0] < grid_width and 0 <= extended[1] < grid_height:
                    antinodes.add(extended)
                else:
                    break
                k += 1
    
    return antinodes

def count_unique_antinodes(grid):
    """
    Count the total number of unique antinodes within the grid.
    """
    antennas = parse_input(grid)
    grid_width, grid_height = len(grid[0]), len(grid)
    unique_antinodes = set()
    
    for freq, positions in antennas.items():
        if len(positions) > 1:  # Only calculate if more than 1 antenna of this frequency
            antinodes = add_antinodes(positions, grid_width, grid_height)
            unique_antinodes.update(antinodes)
    
    return len(unique_antinodes), unique_antinodes

def visualize_grid(grid, antinodes):
    """
    Generate a visual representation of the grid with antinodes marked.
    """
    grid = [list(row) for row in grid]  # Convert to mutable list of lists
    for x, y in antinodes:
        if grid[y][x] == '.':  # Only replace empty cells
            grid[y][x] = '#'
    return '\n'.join(''.join(row) for row in grid)

# Input grid
'''
grid = [
    "............",
    "........0...",
    ".....0......",
    ".......0....",
    "....0.......",
    "......A.....",
    "............",
    "............",
    "........A...",
    ".........A..",
    "............",
    "............"
]
'''

# Solve for the number of unique antinodes
result, antinodes = count_unique_antinodes(grid)
visualized_grid = visualize_grid(grid, antinodes)

print(f"Number of unique antinode locations: {result}")
print("Visualized Grid with Antinodes:")
print(visualized_grid)

