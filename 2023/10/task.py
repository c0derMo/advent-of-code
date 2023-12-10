def task1(input_lines: list[str]):
    grid, starting_position = reconstruct_starting_point(input_lines)
    max_distance = walk_recursively_get_max(grid, starting_position)
    print(max_distance)

def task2(input_lines: list[str]):
    grid, starting_position = reconstruct_starting_point(input_lines)
    print("Figured out start")
    loop = walk_recursively_isolate_loop(grid, starting_position)
    print("Isolated loop")
    replaced_loop = replace_anything_non_main_loop(grid, loop)
    print("Replaced all")
    amount_o = count_O(replaced_loop)
    print("Counted Os")
    result = (len(input_lines) * len(input_lines[0])) - amount_o - len(loop)

    for line in replaced_loop:
        print(line)

    print(result)

def has_connection_north(pipe: str) -> bool:
    return pipe in ["|", "L", "J"]

def has_connection_south(pipe: str) -> bool:
    return pipe in ["|", "F", "7"]

def has_connection_west(pipe: str) -> bool:
    return pipe in ["-", "7", "J"]

def has_connection_east(pipe: str) -> bool:
    return pipe in ["-", "F", "L"]

def get_pipe_connecting(north: bool, south: bool, east: bool, west: bool) -> str:
    if north and south:
        return "|"
    if north and east:
        return "L"
    if north and west:
        return "J"
    if west and east:
        return "-"
    if west and south:
        return "7"
    if south and east:
        return "F"
    return "."

def replace_at(input_string: str, index: int, replacement: str) -> str:
    return input_string[:index] + replacement + input_string[index + 1:]

def reconstruct_starting_point(grid: list[str]) -> tuple[list[str], tuple[int, int]]:
    starting_position = (-1, -1)

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "S":
                starting_position = (x, y)
                break
        if starting_position != (-1, -1):
            break
    
    grid_copy = grid

    N = y > 0 and has_connection_south(grid[y-1][x])
    S = y < len(grid)-1 and has_connection_north(grid[y+1][x])
    W = x > 0 and has_connection_east(grid[y][x-1])
    E = x < len(grid[0])-1 and has_connection_west(grid[y][x+1])

    pipe = get_pipe_connecting(N, S, E, W)
    print(f"Start pipe: {pipe}")


    grid_copy[starting_position[1]] = replace_at(grid_copy[starting_position[1]], starting_position[0], pipe)
    return grid_copy, starting_position

def walk_recursively_get_max(grid: list[str], starting_position: tuple[int, int]) -> int:
    to_visit = [starting_position]
    visited = [starting_position]
    distance = [0]

    while len(to_visit) > 0:
        visit_x, visit_y = to_visit.pop(0)
        index = visited.index((visit_x, visit_y))
        local_distance = distance[index]

        print(f"Reached a distance of {local_distance}")

        if has_connection_north(grid[visit_y][visit_x]) and (visit_x,visit_y-1) not in visited:
            to_visit.append((visit_x,visit_y-1))
            visited.append((visit_x,visit_y-1))
            distance.append(local_distance + 1)
        if has_connection_south(grid[visit_y][visit_x]) and (visit_x,visit_y+1) not in visited:
            to_visit.append((visit_x,visit_y+1))
            visited.append((visit_x,visit_y+1))
            distance.append(local_distance + 1)
        if has_connection_west(grid[visit_y][visit_x]) and (visit_x-1,visit_y) not in visited:
            to_visit.append((visit_x-1,visit_y))
            visited.append((visit_x-1,visit_y))
            distance.append(local_distance + 1)
        if has_connection_east(grid[visit_y][visit_x]) and (visit_x+1,visit_y) not in visited:
            to_visit.append((visit_x+1,visit_y))
            visited.append((visit_x+1,visit_y))
            distance.append(local_distance + 1)
    
    return distance[-1]

def walk_recursively_isolate_loop(grid: list[str], starting_position: tuple[int, int]) -> list[tuple[int, int]]:
    to_visit = [starting_position]
    visited = [starting_position]

    while len(to_visit) > 0:
        visit_x, visit_y = to_visit.pop(0)

        if has_connection_north(grid[visit_y][visit_x]) and (visit_x,visit_y-1) not in visited:
            to_visit.append((visit_x,visit_y-1))
            visited.append((visit_x,visit_y-1))
        if has_connection_south(grid[visit_y][visit_x]) and (visit_x,visit_y+1) not in visited:
            to_visit.append((visit_x,visit_y+1))
            visited.append((visit_x,visit_y+1))
        if has_connection_west(grid[visit_y][visit_x]) and (visit_x-1,visit_y) not in visited:
            to_visit.append((visit_x-1,visit_y))
            visited.append((visit_x-1,visit_y))
        if has_connection_east(grid[visit_y][visit_x]) and (visit_x+1,visit_y) not in visited:
            to_visit.append((visit_x+1,visit_y))
            visited.append((visit_x+1,visit_y))
    
    return visited

def squeeze(grid: list[str], loop: list[tuple[int, int]], current_pos: tuple[int, int], direction: str) -> list[tuple[int, int]]:
    if direction == "t":
        x, y = current_pos
        if y <= 0:
            return [(x, y),(x+1, y)]
        if (x,y) not in loop or (x+1,y) not in loop:
            return [(x, y),(x+1, y)]
        
        # Diagonals
        # if x > 0 and grid[y][x-1] == "L" and grid[y][x] == "7" and grid[y][x+1] == "L" and grid[y-1][x] == "L":
        #     return squeeze(grid, loop, (x-1,y-1), "t")
        # if grid[]

        res = []
        if grid[y][x] in ["|", "J", "7"] and grid[y][x+1] in ["|", "F", "L"]:
            # Walk top
            res.extend(squeeze(grid, loop, (x,y-1), "t"))
        if grid[y][x] == "7" and grid[y-1][x] in ["-", "J", "L"]:
            # Walk left
            res.extend(squeeze(grid, loop, (x,y-1), "l"))
        if grid[y][x+1] == "F" and grid[y-1][x+1] in ["-", "L", "J"]:
            # Walk right
            res.extend(squeeze(grid, loop, (x+1,y-1), "r"))
        if len(res) > 0:
            return res
        
        return [(x, y),(x+1, y)]
    
    if direction == "b":
        x, y = current_pos
        if y >= len(grid)-1:
            return [(x, y),(x+1, y)]
        if (x,y) not in loop or (x+1,y) not in loop:
            return [(x, y),(x+1, y)]
        
        # Diagonals
        # if x < len(grid[0])-2 and grid[y][x] == "7" and grid[y][x+1] == "L" and grid[y][x+2] == "7" and grid[y+1][x] == "L":
        #     return squeeze(grid, loop, (x+1,y+1), "b")

        res = []
        if grid[y][x] in ["|", "J", "7"] and grid[y][x+1] in ["|", "F", "L"]:
            # Walk bottom
            res.extend(squeeze(grid, loop, (x,y+1), "b"))
        if grid[y][x] == "J" and grid[y+1][x] in ["-", "7", "F"]:
            # Walk left
            res.extend(squeeze(grid, loop, (x,y), "l"))
        if grid[y][x+1] == "L" and grid[y+1][x+1] in ["-", "F", "7"]:
            # Walk right
            res.extend(squeeze(grid, loop, (x+1,y), "r"))
        if len(res) > 0:
            return res
        
        return [(x, y),(x+1, y)]

    if direction == "l":
        x, y = current_pos
        if x <= 0:
            return [(x, y),(x, y+1)]
        if (x,y) not in loop or (x,y+1) not in loop:
            return [(x, y),(x, y+1)]
        
        res = []
        if grid[y][x] in ["-", "J", "L"] and grid[y+1][x] in ["-", "F", "7"]:
            # Walk left
            res.extend(squeeze(grid, loop, (x-1,y), "l"))
        if grid[y][x] == "L" and grid[y][x-1] in ["|", "J", "7"]:
            # Walk top
            res.extend(squeeze(grid, loop, (x-1,y), "t"))
        if grid[y+1][x] == "F" and grid[y+1][x-1] in ["|", "7", "J"]:
            # Walk bottom
            res.extend(squeeze(grid, loop, (x-1,y+1), "b"))
        if len(res) > 0:
            return res

        return [(x, y),(x, y+1)]
    
    if direction == "r":
        x, y = current_pos
        if x >= len(grid[0])-1:
            return [(x, y),(x, y+1)]
        if (x,y) not in loop or (x,y+1) not in loop:
            return [(x, y),(x, y+1)]
        
        res = []
        if grid[y][x] in ["-", "J", "L"] and grid[y+1][x] in ["-", "F", "7"]:
            # Walk right
            res.extend(squeeze(grid, loop, (x+1,y), "r"))
        if grid[y][x] == "J" and grid[y][x+1] in ["|", "L", "F"]:
            # Walk top
            res.extend(squeeze(grid, loop, (x,y), "t"))
        if grid[y+1][x] == "7" and grid[y+1][x+1] in ["|", "F", "L"]:
            # Walk bottom
            res.extend(squeeze(grid, loop, (x,y+1), "b"))
        if len(res) > 0:
            return res

        return [(x, y),(x, y+1)]

    raise ValueError("Invalid squeeze direction")

def replace_anything_non_main_loop(grid: list[str], loop: list[tuple[int, int]]) -> list[str]:
    points = []
    for y in range(len(grid)):
        points.append((0,y))
        points.append((len(grid[0])-1,y))
    for x in range(1,len(grid[0])-1):
        points.append((x,0))
        points.append((x,len(grid)-1))

    if all([p in loop for p in points]):
        raise ValueError("We're all screwed, all starting points are part of the loop")
    
    while len(points) > 0:
        current_point = points.pop(0)
        if current_point in loop:
            continue

        x, y = current_point

        if grid[y][x] == "O":
            continue
        
        has_l = x > 0
        has_r = x < len(grid[0])-1
        has_t = y > 0
        has_b = y < len(grid) - 1

        neighbors = []
        if has_t and (x,y-1) not in loop:
            neighbors.append((x, y-1))
        if has_b and (x,y+1) not in loop:
            neighbors.append((x, y+1))
        if has_l and (x-1,y) not in loop:
            neighbors.append((x-1, y))
        if has_r and (x+1,y) not in loop:
            neighbors.append((x+1, y))
        if has_t and has_l and (x-1,y-1) not in loop:
            neighbors.append((x-1,y-1))
        if has_t and has_r and (x+1,y-1) not in loop:
            neighbors.append((x+1,y-1))
        if has_b and has_l and (x-1,y+1) not in loop:
            neighbors.append((x-1,y+1))
        if has_b and has_r and (x+1,y+1) not in loop:
            neighbors.append((x+1,y+1))
        
        # FUCKING SQUEEZING
        if has_t and has_l:
            if (x,y-1) in loop and (x-1,y-1) in loop and grid[y-1][x] in ["L", "|", "F"] and grid[y-1][x-1] in ["|", "J", "7"]:
                neighbors.extend(squeeze(grid, loop, (x-1,y-1), "t"))
            if (x-1,y-1) in loop and (x-1,y) in loop and grid[y-1][x-1] in ["-", "J", "L"] and grid[y][x-1] in ["-", "7", "F"]:
                neighbors.extend(squeeze(grid, loop, (x-1,y-1), "l"))
        if has_t and has_r:
            if (x,y-1) in loop and (x+1,y-1) in loop and grid[y-1][x+1] in ["L", "|", "F"] and grid[y-1][x] in ["|", "J", "7"]:
                neighbors.extend(squeeze(grid, loop, (x,y-1), "t"))
            if (x+1,y-1) in loop and (x+1,y) in loop and grid[y-1][x+1] in ["L", "-", "J"] and grid[y][x+1] in ["-", "F", "7"]:
                neighbors.extend(squeeze(grid, loop, (x+1,y-1), "r"))
        if has_b and has_l:
            if (x,y+1) in loop and (x-1,y+1) in loop and grid[y+1][x-1] in ["7", "|", "J"] and grid[y+1][x] in ["|", "F", "L"]:
                neighbors.extend(squeeze(grid, loop, (x-1,y+1), "b"))
            if (x-1,y) in loop and (x-1,y+1) in loop and grid[y][x-1] in ["-", "J", "L"] and grid[y+1][x-1] in ["-", "7", "F"]:
                neighbors.extend(squeeze(grid, loop, (x-1,y), "l"))
        if has_b and has_r:
            if (x,y+1) in loop and (x+1,y+1) in loop and grid[y+1][x] in ["7", "|", "J"] and grid[y+1][x+1] in ["|", "F", "L"]:
                neighbors.extend(squeeze(grid, loop, (x,y+1), "b"))
            if (x+1,y) in loop and (x+1,y+1) in loop and grid[y][x+1] in ["L", "-", "J"] and grid[y+1][x+1] in ["-", "F", "7"]:
                neighbors.extend(squeeze(grid, loop, (x+1,y), "r"))


        # Check if edge or any neighbor is O
        if not has_l or not has_r or not has_t or not has_b or any([grid[y][x] == "O" for x,y in neighbors]):
            grid[y] = replace_at(grid[y], x, "O")
            points.extend(neighbors)
    return grid

def count_O(grid: list[str]) -> int:
    res = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "O":
                res += 1
    return res