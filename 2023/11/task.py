Grid = list[list[str]]

def task1(input_lines: list[str]):
    grid = rows_to_grid(input_lines)
    grid = expand_cols(grid)
    grid = expand_rows(grid)
    # print_grid(grid)
    galaxies = get_galaxies(grid)

    result = 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            g1 = galaxies[i]
            g2 = galaxies[j]

            result += get_distance_between_galaxies(g1, g2)

    print(result)

def task2(input_lines: list[str]):
    grid = rows_to_grid(input_lines)
    galaxies = get_galaxies(grid)
    empty_rows = get_empty_rows(grid)
    empty_colums = get_empty_columns(grid)

    print(empty_rows)
    print(empty_colums)

    galaxies = expand_galaxies(galaxies, empty_rows, empty_colums)

    result = 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            g1 = galaxies[i]
            g2 = galaxies[j]

            result += get_distance_between_galaxies(g1, g2)

    print(result)


def rows_to_grid(rows: list[str]) -> Grid:
    return [[char for char in row] for row in rows]

def print_grid(grid: Grid):
    for row in grid:
        print("".join(row))

def expand_cols(grid: Grid) -> Grid:
    x = 0
    while x < len(grid[0]):
        has_galaxies = False
        for y in range(len(grid)):
            if grid[y][x] == "#":
                has_galaxies = True
                break
        
        if not has_galaxies:
            for y in range(len(grid)):
                grid[y].insert(x, ".")
            x += 1

        x += 1
    
    return grid

def expand_rows(grid: Grid) -> Grid:
    y = 0
    while y < len(grid):
        has_galaxies = False
        for x in range(len(grid[y])):
            if grid[y][x] == "#":
                has_galaxies = True
                break
        
        if not has_galaxies:
            grid.insert(y, grid[y])
            y += 1
        y += 1
    
    return grid

def get_galaxies(grid: Grid) -> list[tuple[int, int]]:
    result = []

    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == "#":
                result.append((x, y))
    
    return result

def get_empty_columns(grid: Grid) -> list[int]:
    empty_columns = []
    for x in range(len(grid[0])):
        has_galaxies = False
        for y in range(len(grid)):
            if grid[y][x] == "#":
                has_galaxies = True
                break
        
        if not has_galaxies:
            empty_columns.append(x)
    
    return empty_columns

def get_empty_rows(grid: Grid) -> list[int]:
    result = []
    for y in range(len(grid)):
        has_galaxies = False
        for x in range(len(grid[y])):
            if grid[y][x] == "#":
                has_galaxies = True
                break
        
        if not has_galaxies:
            result.append(y)
            
    return result

def expand_galaxies(galaxies: list[tuple[int, int]], empty_rows: list[int], empty_cols: list[int], expansion=999999):
    for g_idx in range(len(galaxies)):
        galaxy = galaxies[g_idx]
        x_increase = 0
        y_increase = 0
        for e_c in empty_cols:
            if galaxy[0] > e_c:
                x_increase += expansion
        for e_r in empty_rows:
            if galaxy[1] > e_r:
                y_increase += expansion
        galaxies[g_idx] = (galaxy[0] + x_increase, galaxy[1] + y_increase)
    return galaxies

def get_distance_between_galaxies(g1: tuple[int, int], g2: tuple[int, int]) -> int:
    dist = abs(g1[0] - g2[0])
    dist += abs(g1[1] - g2[1])
    return dist