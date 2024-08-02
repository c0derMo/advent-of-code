def task1(input_lines: list[str]):
    password = input_lines[0]
    password = increment(password)
    valid = has_iol(password) and contains_non_overlapping_pairs(password) and contains_straight_increments(password)
    while not valid:
        password = increment(password)
        valid = has_iol(password) and contains_non_overlapping_pairs(password) and contains_straight_increments(password)
    print(password)

def task2(input_lines: list[str]):
    password = input_lines[0]
    # Pass 1
    password = increment(password)
    valid = has_iol(password) and contains_non_overlapping_pairs(password) and contains_straight_increments(password)
    while not valid:
        password = increment(password)
        valid = has_iol(password) and contains_non_overlapping_pairs(password) and contains_straight_increments(password)
    # Pass 2
    password = increment(password)
    valid = has_iol(password) and contains_non_overlapping_pairs(password) and contains_straight_increments(password)
    while not valid:
        password = increment(password)
        valid = has_iol(password) and contains_non_overlapping_pairs(password) and contains_straight_increments(password)
    print(password)


def increment(prev: str) -> str:
    last_char = prev[-1]
    stem = prev[:-1]
    numeric_char = ord(last_char)
    numeric_char += 1
    if numeric_char == 105 or numeric_char == 111 or numeric_char == 108:
        numeric_char += 1
    if numeric_char > 122:
        numeric_char = 97
        stem = increment(stem)
    return stem + chr(numeric_char)

def has_iol(test: str) -> bool:
    if "i" in test:
        return False
    if "o" in test:
        return False
    if "l" in test:
        return False
    return True

def contains_non_overlapping_pairs(test: str) -> bool:
    last_char = ""
    pairs = 0

    for char in test:
        if char == last_char:
            pairs += 1
            last_char = ""
        else:
            last_char = char
        
        if pairs == 2:
            return True
    return False


def contains_straight_increments(test: str) -> bool:
    last_char = 0
    in_a_row = 0

    for char in test:
        numeric_char = ord(char)
        if numeric_char - 1 == last_char:
            in_a_row += 1
        else:
            in_a_row = 0
        
        last_char = numeric_char
        if in_a_row == 2:
            return True

    return False