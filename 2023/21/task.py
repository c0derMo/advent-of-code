import math

def task1(input_lines: list[str]):
    start = find_start(input_lines)
    reachable = endable_in(input_lines, start)
    print(reachable)

def task2(input_lines: list[str]):
    start = find_start(input_lines)
    grid_size = len(input_lines)
    steps = 26501365

    num_full_grids = math.floor(steps / grid_size) - 1

    odd_grids = 1
    even_grids = 0
    o = False
    for i in range(num_full_grids):
        if o:
            odd_grids += 4 * (i+1)
        else:
            even_grids += 4 * (i+1)
        o = not o

    result = 0

    result += endable_in(input_lines, (start[0], 0), grid_size - 1)
    result += endable_in(input_lines, (start[0], grid_size-1), grid_size - 1)
    result += endable_in(input_lines, (0, start[1]), grid_size - 1)
    result += endable_in(input_lines, (grid_size-1, start[1]), grid_size - 1)
    print("Done corners")

    half_grid = math.floor(grid_size / 2.0) - 1
    print(half_grid)

    result += num_full_grids * endable_in(input_lines, (0,0), grid_size + half_grid)
    result += num_full_grids * endable_in(input_lines, (grid_size-1,0), grid_size + half_grid)
    result += num_full_grids * endable_in(input_lines, (0,grid_size-1), grid_size + half_grid)
    result += num_full_grids * endable_in(input_lines, (grid_size-1,grid_size-1), grid_size + half_grid)
    print("Done edges")

    result += (num_full_grids+1) * endable_in(input_lines, (0,0), half_grid)
    result += (num_full_grids+1) * endable_in(input_lines, (grid_size-1,0), half_grid)
    result += (num_full_grids+1) * endable_in(input_lines, (0,grid_size-1), half_grid)
    result += (num_full_grids+1) * endable_in(input_lines, (grid_size-1,grid_size-1), half_grid)

    result += even_grids * get_reachable_in_full_grid(input_lines, start, True)
    result += odd_grids * get_reachable_in_full_grid(input_lines, start)
    print("Done full grids")
    
    print(result)


def find_start(grid: list[str]) -> tuple[int, int]:
    for y, row in enumerate(grid):
        for x, sym in enumerate(row):
            if sym == "S":
                return (x, y)
    raise ValueError("No starting location found")

GARDENABLE = ['.', 'S']

def endable_in(grid: list[str], starting_position: tuple[int, int], steps=64) -> int:
    visited = []
    for _ in range(len(grid)):
        row = []
        for _ in range(len(grid[0])):
            row.append(False)
        visited.append(row)
    
    x_max = len(grid[0])-1
    y_max = len(grid)-1

    v1 = 0
    v2 = 0
    current_v = False

    new_reachable = [starting_position]
    next_iteration = []
    current_steps = 0

    while current_steps < steps:
        current_steps += 1
        
        for reachable in new_reachable:
            x, y = reachable

            visited[y][x] = True
            if current_v:
                v2 += 1
            else:
                v1 += 1

            if x > 0 and grid[y][x-1] in GARDENABLE and (x-1, y) not in next_iteration and not visited[y][x-1]:
                next_iteration.append((x-1, y))
            if x < x_max and grid[y][x+1] in GARDENABLE and (x+1, y) not in next_iteration and not visited[y][x+1]:
                next_iteration.append((x+1, y))
            if y > 0 and grid[y-1][x] in GARDENABLE and (x, y-1) not in next_iteration and not visited[y-1][x]:
                next_iteration.append((x, y-1))
            if y < y_max and grid[y+1][x] in GARDENABLE and (x, y+1) not in next_iteration and not visited[y+1][x]:
                next_iteration.append((x, y+1))
        
        new_reachable = [x for x in next_iteration]
        next_iteration.clear()
        current_v = not current_v
    
    # for y, row in enumerate(grid):
    #     r = ""
    #     for x, sym in enumerate(row):
    #         if (x, y) in new_reachable:
    #             r += "O"
    #         else:
    #             r += sym
    #     print(r)

    if current_v:
        return v2 + len(new_reachable)
    else:
        return v1 + len(new_reachable)


def get_reachable_in_full_grid(grid: list[str], starting_position: tuple[int, int], invert=False) -> int:
    visited = []
    for _ in range(len(grid)):
        row = []
        for _ in range(len(grid[0])):
            row.append(False)
        visited.append(row)

    x_max = len(grid[0])-1
    y_max = len(grid)-1

    now_visiting = [starting_position]
    visiting_next = []
    currently_reachable = invert
    all_reachable = 0

    while len(now_visiting) != 0:
        for visiting in now_visiting:
            x, y = visiting
            visited[y][x] = True
            if currently_reachable:
                all_reachable += 1
            if x > 0 and grid[y][x-1] in GARDENABLE and (x-1, y) not in visiting_next and not visited[y][x-1]:
                visiting_next.append((x-1, y))
            if x < x_max and grid[y][x+1] in GARDENABLE and (x+1, y) not in visiting_next and not visited[y][x+1]:
                visiting_next.append((x+1, y))
            if y > 0 and grid[y-1][x] in GARDENABLE and (x, y-1) not in visiting_next and not visited[y-1][x]:
                visiting_next.append((x, y-1))
            if y < y_max and grid[y+1][x] in GARDENABLE and (x, y+1) not in visiting_next and not visited[y+1][x]:
                visiting_next.append((x, y+1))

        now_visiting = [x for x in visiting_next]
        visiting_next.clear()
        currently_reachable = not currently_reachable

    return all_reachable