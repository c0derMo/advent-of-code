def task1(input_lines: list[str]):
    reports = [[int(x) for x in y.split()] for y in input_lines]

    save = 0
    for report in reports:
        if is_safe(report):
            save += 1
    print(save)

def task2(input_lines: list[str]):
    reports = [[int(x) for x in y.split()] for y in input_lines]

    bfs = []
    for report in reports:
        if is_safe_dampened_bf(report):
        # if is_safe_dampened_bf(report) and not is_safe_dampened(report):
            bfs.append(report)
    
    # print(bfs)
    print(len(bfs))

def is_safe(levels: list[int]) -> bool:
    increasing = True
    if levels[0] > levels[1]:
        increasing = False
    
    for i in range(len(levels)-1):
        if levels[i] > levels[i+1] and increasing:
            return False
        if levels[i] < levels[i+1] and not increasing:
            return False
        if abs(levels[i] - levels[i+1]) > 3 or abs(levels[i] - levels[i+1]) < 1:
            return False
    return True

def is_safe_dampened_bf(levels: list[int]) -> bool:
    if is_safe(levels):
        return True
    
    for i in range(len(levels)):
        new_range = levels[:i]
        new_range.extend(levels[i+1:])
        if is_safe(new_range):
            return True