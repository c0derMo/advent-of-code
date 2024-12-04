import re

rect_re = re.compile(r"rect (\d+)x(\d+)")
rot_col_re = re.compile(r"rotate column x=(\d+) by (\d+)")
rot_row_re = re.compile(r"rotate row y=(\d+) by (\d+)")

def task1(input_lines: list[str]):
    screen = create_screen(50, 6)
    # screen = create_screen(7, 3)

    for line in input_lines:
        rect_matcher = rect_re.match(line)
        rot_col_matcher = rot_col_re.match(line)
        rot_row_matcher = rot_row_re.match(line)
        if rect_matcher is not None:
            screen = turn_rect_on(int(rect_matcher.group(1)), int(rect_matcher.group(2)), screen)
        elif rot_col_matcher is not None:
            screen = rot_col(int(rot_col_matcher.group(1)), int(rot_col_matcher.group(2)), screen)
        elif rot_row_matcher is not None:
            screen = rot_row(int(rot_row_matcher.group(1)), int(rot_row_matcher.group(2)), screen)
        # print_screen(screen)
        # print("")
    
    print_screen(screen)
    count = 0
    for y in screen:
        for x in y:
            if x:
                count += 1

    print(count)

def task2(input_lines: list[str]):
    print("Unimplemented")

def print_screen(screen: list[list[bool]]):
    for row in screen:
        r = ""
        for x in row:
            if x:
                r += "#"
            else:
                r += "."
        print(r)

def create_screen(w: int, h: int) -> list[list[bool]]:
    screen = []
    for _ in range(h):
        row = []
        for _ in range(w):
            row.append(False)
        screen.append(row)
    return screen

def turn_rect_on(w: int, h: int, screen: list[list[bool]]) -> list[list[bool]]:
    for x in range(w):
        for y in range(h):
            screen[y][x] = True
    return screen

def rot_row(row: int, length: int, screen: list[list[bool]]) -> list[list[bool]]:
    screen[row].insert(0, screen[row].pop())
    if length > 1:
        return rot_row(row, length-1, screen)
    return screen

def rot_col(col: int, length: int, screen: list[list[bool]]) -> list[list[bool]]:
    prev = screen[len(screen)-1][col]
    for y in range(len(screen)):
        temp = screen[y][col]
        screen[y][col] = prev
        prev = temp
    if length > 1:
        return rot_col(col, length-1, screen)
    return screen