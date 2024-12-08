#!/usr/bin/env python3

def parse_input(grid):
    """
    Parse the input grid into a dictionary of frequencies and their coordinates.
    """
    antennas = {}
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell != '.':
                if cell not in antennas:
                    antennas[cell] = []
                antennas[cell].append((x, y))
    return antennas

def calculate_antinodes(antenna_positions):
    """
    Calculate all unique antinode positions for a given list of antenna positions.
    """
    antinodes = set()
    
    for i in range(len(antenna_positions)):
        for j in range(len(antenna_positions)):
            if i == j:
                continue
            x1, y1 = antenna_positions[i]
            x2, y2 = antenna_positions[j]
            
            # Compute possible antinode positions if one antenna is twice as far as the other
            dx, dy = x2 - x1, y2 - y1
            
            # Antinodes are on the line extended past the antennas
            antinode1 = (x1 - dx, y1 - dy)  # Extend towards the first antenna
            antinode2 = (x2 + dx, y2 + dy)  # Extend past the second antenna
            
            antinodes.add(antinode1)
            antinodes.add(antinode2)
    
    return antinodes

def count_unique_antinodes(grid):
    """
    Count all unique antinodes within the bounds of the grid.
    """
    antennas = parse_input(grid)
    unique_antinodes = set()
    
    for freq, positions in antennas.items():
        antinodes = calculate_antinodes(positions)
        
        # Filter antinodes to ensure they're within the grid bounds
        for x, y in antinodes:
            if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
                unique_antinodes.add((x, y))
    
    return len(unique_antinodes)

# Example input
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

def load_file_to_2d_array(file_path):
    array = [] 
    with open(file_path, 'r') as file:
        for line in file:
            array.append(list(line.rstrip()))
    return array    
                
grid = load_file_to_2d_array('day_8_input.txt')

# Compute and print the result
result = count_unique_antinodes(grid)
print(f"Number of unique antinode locations: {result}")

