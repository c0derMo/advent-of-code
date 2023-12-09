def task1(input_lines: list[str]):
    result = 0

    for line in input_lines:
        parsed_line = [int(x) for x in line.split()]
        ex_down = extrapolate_down(parsed_line)
        print(ex_down)
        ex_up = extrapolate_up(ex_down)
        print(ex_up)
        result += ex_up[0][-1]
    print(result)

def task2(input_lines: list[str]):
    result = 0

    for line in input_lines:
        parsed_line = [int(x) for x in line.split()]
        ex_down = extrapolate_down(parsed_line)
        print(ex_down)
        ex_up = extrapolate_up_left(ex_down)
        print(ex_up)
        result += ex_up[0][0]
    print(result)


def extrapolate_down(history: list[int]) -> list[list[int]]:
    result = [history]
    while not all([x == 0 for x in result[-1]]):
        new_list = []
        for i in range(0, len(result[-1])-1):
            new_list.append(result[-1][i + 1] - result[-1][i])
        result.append(new_list)
    return result

def extrapolate_up(numbers: list[list[int]]) -> list[list[int]]:
    result = numbers
    result[-1].append(0)
    for i in range(len(result)-2, -1, -1):
        result[i].append(result[i][-1] + result[i+1][-1])
    return result

def extrapolate_up_left(numbers: list[list[int]]) -> list[list[int]]:
    result = numbers
    result[-1].insert(0, 0)
    for i in range(len(result)-2, -1, -1):
        result[i].insert(0, result[i][0] - result[i+1][0])
    return result