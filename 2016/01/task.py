def task1(input_lines: list[str]):
    instructions = input_lines[0].split(", ")

    facing = 0
    x = 0
    y = 0
    for instruction in instructions:
        if instruction[0] == "R":
            facing = (facing + 1) % 4
        elif instruction[0] == "L":
            facing = (facing - 1) % 4
        else:
            raise ValueError(f"Invalid direction: {instruction}")
        
        distance = int(instruction[1:])
        if facing >= 2:
            distance = -distance
        if facing % 2 == 0:
            y += distance
        else:
            x += distance
        
    print(x + y)

def task2(input_lines: list[str]):
    instructions = input_lines[0].split(", ")

    facing = 0
    x = 0
    y = 0
    visited: set[tuple[int, int]] = set()
    for instruction in instructions:
        if instruction[0] == "R":
            facing = (facing + 1) % 4
        elif instruction[0] == "L":
            facing = (facing - 1) % 4
        else:
            raise ValueError(f"Invalid direction: {instruction}")
        distance = int(instruction[1:])
        for i in range(distance):
            if facing == 0:
                new_pos = (x, y+1)
            elif facing == 1:
                new_pos = (x+1, y)
            elif facing == 2:
                new_pos = (x, y-1)
            elif facing == 3:
                new_pos = (x-1, y)
            
            if new_pos in visited:
                print(abs(new_pos[0]) + abs(new_pos[1]))
                return
            else:
                visited.add(new_pos)
            
            x = new_pos[0]
            y = new_pos[1]

    print("No solution :/")