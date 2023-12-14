import math

PrecalcMap = dict[tuple[int, int], tuple[tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int]]]

def task1(input_lines: list[str]):
    rocks, blocks = parse_grid(input_lines)
    rocks = roll_north(rocks, blocks)
    load = calculate_load_north(rocks, len(input_lines))
    print(load)

cache: dict[tuple[tuple[int, int], ...], int] = {}

def task2(input_lines: list[str]):
    rocks, blocks = parse_grid(input_lines)

    y_len = len(input_lines)
    x_len = len(input_lines[0])

    calculated_map = precalc_spots(blocks, y_len, x_len)
    print("Pre calc done")
            
    iters = 1000000000

    i = 0
    while i < iters:
        rocks = roll_cycle_with_map(rocks, calculated_map)
        t_rocks = tuple(rocks)

        if t_rocks in cache:
            # POG WE GOT A CACHE HIT
            i_diff = i - cache[t_rocks]
            print(f"cache hit with idiff {i_diff}")

            times = math.floor((iters - i) / i_diff)
            i += times * i_diff
        else:
            cache[t_rocks] = i

        print(i)

        i += 1

    load = calculate_load_north(rocks, len(input_lines))
    print(load)

def parse_grid(grid: list[str]) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
    rocks = []
    blocks = []

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "O":
                rocks.append((x, y))
            if grid[y][x] == "#":
                blocks.append((x, y))

    return rocks, blocks

def print_grid(rocks: list[tuple[int, int]], blocks: list[tuple[int, int]], y_len: int, x_len: int):
    for y in range(y_len):
        line = ""
        for x in range(x_len):
            if (x, y) in rocks:
                line += "O"
            elif (x, y) in blocks:
                line += "#"
            else:
                line += "."
        print(line)
    print("=======")

def roll_north(rocks: tuple[tuple[int, int], ...], blocks: tuple[tuple[int, int], ...]) -> list[tuple[int, int]]:
    sorted_rocks = sorted(rocks, key=lambda x: x[1])
    result = []

    for rock in sorted_rocks:
        new_x, new_y = rock
        while new_y > 0:
            if (new_x, new_y - 1) not in blocks and (new_x, new_y - 1) not in result:
                new_y -= 1
            else:
                break
        result.append((new_x, new_y))
    return result

def calculate_load_north(rocks: list[tuple[int, int]], y_len: int) -> int:
    load = 0
    for rock in rocks:
        load += y_len - rock[1]
    return load

def precalc_spots(blocks: list[tuple[int, int]], y_len: int, x_len: int) -> PrecalcMap:
    M = {}

    for y in range(y_len):
        for x in range(x_len):
            result = []

            y_north = y
            while y_north > 0:
                if (x, y_north - 1) not in blocks:
                    y_north -= 1
                else:
                    break
            y_south = y
            while y_south < y_len - 1:
                if (x, y_south + 1) not in blocks:
                    y_south += 1
                else:
                    break
            x_west = x
            while x_west > 0:
                if (x_west - 1, y) not in blocks:
                    x_west -= 1
                else:
                    break
            x_east = x
            while x_east < x_len - 1:
                if (x_east + 1, y) not in blocks:
                    x_east += 1
                else:
                    break
            result.append((x, y_north))
            result.append((x, y_south))
            result.append((x_west, y))
            result.append((x_east, y))

            M[(x, y)] = tuple(result)
    return M

def roll_cycle_with_map(rocks: list[tuple[int, int]], m: PrecalcMap) -> list[tuple[int, int]]:
    rocks = roll_north_map(tuple(rocks), m)
    rocks = roll_west_map(tuple(rocks), m)
    rocks = roll_south_map(tuple(rocks), m)
    rocks = roll_east_map(tuple(rocks), m)
    return rocks


def roll_north_map(rocks: tuple[tuple[int, int], ...], m: PrecalcMap) -> list[tuple[int, int]]:
    sorted_rocks = sorted(rocks, key=lambda x: x[1])
    result = []

    for rock in sorted_rocks:
        new_x, new_y = m[rock][0]
        while (new_x, new_y) in result:
            new_y += 1
        result.append((new_x, new_y))
    return result

def roll_south_map(rocks: tuple[tuple[int, int], ...], m: PrecalcMap) -> list[tuple[int, int]]:
    sorted_rocks = sorted(rocks, key=lambda x: x[1], reverse=True)
    result = []

    for rock in sorted_rocks:
        new_x, new_y = m[rock][1]
        while (new_x, new_y) in result:
            new_y -= 1
        result.append((new_x, new_y))

    return result

def roll_west_map(rocks: tuple[tuple[int, int], ...], m: PrecalcMap) -> list[tuple[int, int]]:
    sorted_rocks = sorted(rocks, key=lambda x: x[0])
    result = []

    for rock in sorted_rocks:
        new_x, new_y = m[rock][2]
        while (new_x, new_y) in result:
            new_x += 1
        result.append((new_x, new_y))
    return result

def roll_east_map(rocks: tuple[tuple[int, int], ...], m: PrecalcMap) -> list[tuple[int, int]]:
    sorted_rocks = sorted(rocks, key=lambda x: x[0], reverse=True)
    result = []

    for rock in sorted_rocks:
        new_x, new_y = m[rock][3]
        while (new_x, new_y) in result:
            new_x -= 1
        result.append((new_x, new_y))
    return result