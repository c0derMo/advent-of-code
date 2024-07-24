def task1(input_lines: list[str]):
    nice = 0
    for line in input_lines:
        if is_nice(line):
            nice += 1
    print(nice)

def task2(input_lines: list[str]):
    nice = 0
    for line in input_lines:
        if is_nice_mk2(line):
            nice += 1
    print(nice)

def is_nice(check: str) -> bool:
    if "ab" in check:
        return False
    if "cd" in check:
        return False
    if "pq" in check:
        return False
    if "xy" in check:
        return False
    
    has_double = False
    vowls = 0
    for i in range(len(check)-1):
        if check[i] == check[i+1]:
            has_double = True
        if check[i] in ["a", "e", "i", "o", "u"]:
            vowls += 1
        if has_double and vowls >= 3:
            break
    if check[len(check)-1] in ["a", "e", "i", "o", "u"]:
        vowls += 1

    return has_double and vowls >= 3

def is_nice_mk2(check: str) -> bool:
    has_doubled_pair = False
    for i in range(len(check)-3):
        pair = check[i] + check[i+1]
        for j in range(i+2, len(check)-1):
            if check[j] + check[j+1] == pair:
                has_doubled_pair = True
                break
        if has_doubled_pair:
            break
    
    if not has_doubled_pair:
        return False
    
    has_repeating_with_seperator = False
    for i in range(len(check)-2):
        if check[i] == check[i+2]:
            has_repeating_with_seperator = True
            break
    
    return has_doubled_pair and has_repeating_with_seperator