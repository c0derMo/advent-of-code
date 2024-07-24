def task1(input_lines: list[str]):
    target_floor = find_target_floor(input_lines[0])
    print(target_floor)

def task2(input_lines: list[str]):
    target_floor = find_first_basement(input_lines[0])
    print(target_floor)


def find_target_floor(line: str) -> int:
    current_floor = 0
    for char in line:
        if char == "(":
            current_floor += 1
        elif char == ")":
            current_floor -= 1
        else:
            print(f"Illegal char! {char}")
    return current_floor

def find_first_basement(line: str) -> int:
    current_floor = 0
    for idx, char in enumerate(line):
        if char == "(":
            current_floor += 1
        elif char == ")":
            current_floor -= 1
        else:
            print(f"Illegal char! {char}")

        if current_floor < 0:
            return idx+1
        
    return -1