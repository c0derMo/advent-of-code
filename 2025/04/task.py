ROLL = "@"

def task1(input_lines: list[str]):
    accessible = get_accessible_rolls(input_lines)
    print(len(accessible))

def task2(input_lines: list[str]):
    sum_accessible = 0
    accessible = get_accessible_rolls(input_lines)
    while len(accessible) > 0:
        sum_accessible += len(accessible)
        for y,x in accessible:
            input_lines[y] = input_lines[y][:x] + "#" + input_lines[y][x+1:]
        # for line in input_lines:
        #     print(line)
        # print("===")
        accessible = get_accessible_rolls(input_lines)

    print(sum_accessible)

def get_accessible_rolls(grid: list[str]) -> list[tuple[int, int]]:
    accessible: list[tuple[int, int]] = []

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != ROLL:
                continue

            adjacent = 0
            # L
            if x > 0 and grid[y][x-1] == ROLL:
                adjacent += 1
            # R
            if x < len(grid[y])-1 and grid[y][x+1] == ROLL:
                adjacent += 1
            # T
            if y > 0 and grid[y-1][x] == ROLL:
                adjacent += 1
            # B
            if y < len(grid)-1 and grid[y+1][x] == ROLL:
                adjacent += 1
                
            # TL
            if y > 0 and x > 0 and grid[y-1][x-1] == ROLL:
                adjacent += 1
            # TR
            if y > 0 and x < len(grid[y])-1 and grid[y-1][x+1] == ROLL:
                adjacent += 1
            # BL
            if y < len(grid)-1 and x > 0 and grid[y+1][x-1] == ROLL:
                adjacent += 1
            # TR
            if y < len(grid)-1 and x < len(grid[y])-1 and grid[y+1][x+1] == ROLL:
                adjacent += 1
            
            if adjacent < 4:
                accessible.append((y, x))

    return accessible