def task1(input_lines: list[str]):
    total_sqft = 0
    for line in input_lines:
        total_sqft += calculate_required_sqft(line)
    print(total_sqft)

def task2(input_lines: list[str]):
    total_length = 0
    for line in input_lines:
        total_length += calculate_required_ribbon(line)
    print(total_length)


def calculate_required_sqft(input: str) -> int:
    splitted_input = input.split("x")
    l = int(splitted_input[0])
    w = int(splitted_input[1])
    h = int(splitted_input[2])

    side_1 = l * w
    side_2 = w * h
    side_3 = h * l

    general_area = 2*side_1 + 2*side_2 + 2*side_3
    return general_area + min(side_1, side_2, side_3)

def calculate_required_ribbon(input: str) -> int:
    splitted_input = input.split("x")
    l = int(splitted_input[0])
    w = int(splitted_input[1])
    h = int(splitted_input[2])

    if max(l, w, h) == l:
        return 2*w + 2*h + l*w*h
    elif max(l, w, h) == w:
        return 2*l + 2*h + l*w*h
    else:
        return 2*l + 2*w + l*w*h