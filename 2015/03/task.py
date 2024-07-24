def task1(input_lines: list[str]):
    all_positions = get_visited_houses(input_lines[0])
    print(all_positions)

def task2(input_lines: list[str]):
    all_positions = get_visited_houses_by_two(input_lines[0])
    print(all_positions)

def get_visited_houses(path: str) -> int:
    positions = set()
    x = 0
    y = 0
    positions.add((x, y))
    for char in path:
        if char == "^":
            y += 1
        elif char == "v":
            y -= 1
        elif char == "<":
            x -= 1
        elif char == ">":
            x += 1
        else:
            print(f"Unknown movement char: {char}")
        
        positions.add((x, y))
    return len(positions)

def get_visited_houses_by_two(path: str) -> int:
    positions = set()
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    turn = True
    positions.add((x1, y1))
    for char in path:
        if char == "^":
            if turn:
                y1 += 1
            else:
                y2 += 1
        elif char == "v":
            if turn:
                y1 -= 1
            else:
                y2 -= 1
        elif char == "<":
            if turn:
                x1 -= 1
            else:
                x2 -= 1
        elif char == ">":
            if turn:
                x1 += 1
            else:
                x2 += 1
        else:
            print(f"Unknown movement char: {char}")
        
        positions.add((x1, y1))
        positions.add((x2, y2))
        turn = not turn
    return len(positions)