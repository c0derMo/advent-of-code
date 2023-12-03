import re

def task1(input_lines: list[str]):
    print(is_symbol("."))
    print(is_symbol("0"))
    print(is_digit("0"))
    total_sum = 0

    for y in range(len(input_lines)):
        x = 0
        while x < len(input_lines[0]):
            if is_digit(input_lines[y][x]):
                found_symbol, num, num_len = walk_right_find_symbol(x, y, input_lines, False)
                if found_symbol:
                    print(f"SYM: {num}")
                    total_sum += num
                else:
                    print(f"NOS: {num}")
                x += num_len
            else:
                x += 1
    print(total_sum)

def task2(input_lines: list[str]):
    gears: dict[(int, int), list[int]] = {}

    for y in range(len(input_lines)):
        x = 0
        while x < len(input_lines[0]):
            if is_digit(input_lines[y][x]):
                found_gear, num, num_len = walk_right_find_gear(x, y, input_lines, None)
                if found_gear != None:
                    print(f"GEAR: {num}")
                    if found_gear not in gears:
                        gears[found_gear] = [num]
                    else:
                        gears[found_gear].append(num)
                else:
                    print(f"NOGR: {num}")
                x += num_len
            else:
                x += 1

    gr_sum = 0

    for gear, nums in gears.items():
        if len(nums) == 2:
            gear_ratio = nums[0] * nums[1]
            print(f"Gear ratio: {gear_ratio}")
            gr_sum += gear_ratio
    
    print(gr_sum)

def walk_right_find_symbol(x: int, y: int, grid: list[str], symbol_found: bool) -> (bool, int, int):
    new_found_symbol = symbol_found
    if (not new_found_symbol) and x > 0 and is_symbol(grid[y][x-1]): # Check for symbol left
        new_found_symbol = True
    if (not new_found_symbol) and y > 0 and is_symbol(grid[y-1][x]): # Check for symbol above
        new_found_symbol = True
    if (not new_found_symbol) and y < len(grid)-1 and is_symbol(grid[y+1][x]): # Check for symbol below
        new_found_symbol = True
    if (not new_found_symbol) and x > 0 and y > 0 and is_symbol(grid[y-1][x-1]): # Check for symbol topleft
        new_found_symbol = True
    if (not new_found_symbol) and x > 0 and y < len(grid)-1 and is_symbol(grid[y+1][x-1]): # Check for symbol bottomleft
        new_found_symbol = True
    if (not new_found_symbol) and x < len(grid[0])-1 and y > 0 and is_symbol(grid[y-1][x+1]): # Check for symbol topright
        new_found_symbol = True
    if (not new_found_symbol) and x < len(grid[0])-1 and y < len(grid)-1 and is_symbol(grid[y+1][x+1]): # Check for symbol bottomright
        new_found_symbol = True
    
    if x < len(grid[0])-1 and is_digit(grid[y][x+1]):
        found_symbol, num, prev_len = walk_right_find_symbol(x+1, y, grid, new_found_symbol)
        return (found_symbol, int(grid[y][x]) * (10 ** prev_len) + num, prev_len+1)
    elif x < len(grid[0])-1 and is_symbol(grid[y][x+1]):
        return (True, int(grid[y][x]), 1)
    else:
        return (new_found_symbol, int(grid[y][x]), 1)

def walk_right_find_gear(x: int, y: int, grid: list[str], found_gear: (int, int)) -> ((int, int), int, int):
    new_found_gear = found_gear
    if new_found_gear == None and x > 0 and is_gear(grid[y][x-1]): # Check for symbol left
        new_found_gear = (x-1, y)
    if new_found_gear == None and y > 0 and is_gear(grid[y-1][x]): # Check for symbol above
        new_found_gear = (x, y-1)
    if new_found_gear == None and y < len(grid)-1 and is_gear(grid[y+1][x]): # Check for symbol below
        new_found_gear = (x, y+1)
    if new_found_gear == None and x > 0 and y > 0 and is_gear(grid[y-1][x-1]): # Check for symbol topleft
        new_found_gear = (x-1, y-1)
    if new_found_gear == None and x > 0 and y < len(grid)-1 and is_gear(grid[y+1][x-1]): # Check for symbol bottomleft
        new_found_gear = (x-1, y+1)
    if new_found_gear == None and x < len(grid[0])-1 and y > 0 and is_gear(grid[y-1][x+1]): # Check for symbol topright
        new_found_gear = (x+1, y-1)
    if new_found_gear == None and x < len(grid[0])-1 and y < len(grid)-1 and is_gear(grid[y+1][x+1]): # Check for symbol bottomright
        new_found_gear = (x+1, y+1)

    if x < len(grid[0])-1 and is_digit(grid[y][x+1]):
        gear, num, prev_len = walk_right_find_gear(x+1, y, grid, new_found_gear)
        return (gear, int(grid[y][x]) * (10 ** prev_len) + num, prev_len+1)
    elif x < len(grid[0])-1 and is_gear(grid[y][x+1]):
        return ((x+1, y), int(grid[y][x]), 1)
    else:
        return (new_found_gear, int(grid[y][x]), 1)


def is_symbol(c: str) -> bool:
    return re.compile(r"[^0-9\.]").match(c) != None

def is_digit(c: str) -> bool:
    return re.compile(r"[0-9]").match(c) != None

def is_gear(c: str) -> bool:
    return re.compile(r"\*").match(c) != None