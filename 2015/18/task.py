def task1(input_lines: list[str]):
    grid = build_grid(input_lines)
    # print_grid(grid)

    for _ in range(100):
        # print("---")
        grid = build_following_grid(grid)
        # print_grid(grid)
    
    amount_on = 0
    for row in grid:
        for lamp in row:
            if lamp:
                amount_on += 1
    print(amount_on)

def task2(input_lines: list[str]):
    grid = build_grid(input_lines)

    height = len(grid)-1
    width = len(grid[0])-1

    grid[0][0] = True
    grid[0][width] = True
    grid[height][0] = True
    grid[height][width] = True
    
    for _ in range(100):
        grid = build_following_grid(grid)
        grid[0][0] = True
        grid[0][width] = True
        grid[height][0] = True
        grid[height][width] = True
    
    amount_on = 0
    for row in grid:
        for lamp in row:
            if lamp:
                amount_on += 1
    print(amount_on)

def build_grid(input_lines: list[str]) -> list[list[bool]]:
    grid = []
    for y in range(len(input_lines)):
        row = []
        for char in input_lines[y]:
            if char == "#":
                row.append(True)
            elif char == ".":
                row.append(False)
            else:
                raise ValueError(f"{char} is no valid light")
        grid.append(row)
    return grid

def build_following_grid(current_grid: list[list[bool]]) -> list[list[bool]]:
    new_grid = []

    width = len(current_grid[0])-1
    height = len(current_grid)-1

    for y in range(height+1):
        new_row = []
        for x in range(width+1):
            # print(f"Checking {y} {x}")
            lamps_on = 0
            if x > 0 and current_grid[y][x-1]:
                lamps_on += 1
            if x < width and current_grid[y][x+1]:
                lamps_on += 1
            if y > 0 and current_grid[y-1][x]:
                lamps_on += 1
            if y < height and current_grid[y+1][x]:
                lamps_on += 1
            if x > 0 and y > 0 and current_grid[y-1][x-1]:
                lamps_on += 1
            if x > 0 and y < height and current_grid[y+1][x-1]:
                lamps_on += 1
            if x < width and y > 0 and current_grid[y-1][x+1]:
                lamps_on += 1
            if x < width and y < height and current_grid[y+1][x+1]:
                lamps_on += 1
            
            if lamps_on == 3 or (current_grid[y][x] and lamps_on == 2):
                new_row.append(True)
            else:
                new_row.append(False)
        new_grid.append(new_row)
    
    return new_grid

def print_grid(grid: list[list[bool]]) -> None:
    for row in grid:
        r = ""
        for lamp in row:
            if lamp:
                r += "#"
            else:
                r += "."
        print(r)