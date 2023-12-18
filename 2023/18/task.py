def task1(input_lines: list[str]):
    instructions = input_to_dig_instructions(input_lines)
    area = dig_and_calculate_area(instructions)
    print(area)

def task2(input_lines: list[str]):
    instructions = input_to_better_instructions(input_lines)
    print(instructions)
    area = dig_and_calculate_area(instructions)
    print(area)

def input_to_dig_instructions(input_lines: list[str]) -> list[tuple[str, int]]:
    instructions = []
    for line in input_lines:
        line_split = line.split(" ")
        instructions.append((line_split[0], int(line_split[1])))
    return instructions


def input_to_better_instructions(input_lines: list[str]) -> list[tuple[str, int]]:
    instructions = []
    for line in input_lines:
        hex_num = line.split(" ")[2][2:-1]

        direction_encoded = hex_num[-1]
        length = int(hex_num[:-1], 16)
        match direction_encoded:
            case "0":
                direction = "R"
            case "1":
                direction = "D"
            case "2":
                direction = "L"
            case "3":
                direction = "U"
        
        instructions.append((direction, length))
    return instructions


def dig_and_calculate_area(dig_instructions: list[tuple[str, int]]) -> int:
    area = 1
    width = 1

    for direction, length in dig_instructions:
        if direction == "R":
            width += length
            area += length
        elif direction == "D":
            area += width * length
        elif direction == "L":
            width -= length
        elif direction == "U":
            area -= (width-1) * length
    
    return area