import time
import copy
grid = [
    [0, 0, 0, 0, 0, 0],  
    [0, 0, 1, 0, 0, 0],  
    [0, 0, 1, 1, 0, 0],  
    [0, 1, 1, 0, 0, 0],  
    [0, 0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0, 0]   
]
ROWS = 6
COLS = 6
def print_grid(g):
    for row in g:
        print("".join([' ' if cell else ' ' for cell in row]))
    print("\n" + "-" * COLS)

def count_neighbors(g, x, y):
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < ROWS and 0 <= ny < COLS:
                count += g[nx][ny]
    return count
def next_gen(current):
    new_grid = copy.deepcopy(current)
    for x in range(ROWS):
        for y in range(COLS):
            neighbors = count_neighbors(current, x, y)
            if current[x][y] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[x][y] = 0 
            else:
                if neighbors == 3:
                    new_grid[x][y] = 1  
    return new_grid
generations = 4
for i in range(generations):
    print(f"Generation {i + 1}:")
    print_grid(grid)
    time.sleep(1)
    grid = next_gen(grid)
