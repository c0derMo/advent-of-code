def task1(input_lines: list[str]):
    patterns = [[]]
    for line in input_lines:
        if line == "":
            patterns.append([])
        else:
            patterns[-1].append(line)
    print(f"Got {len(patterns)} patterns.")
    result = 0
    for idx, pattern in enumerate(patterns):
        row_reflection = try_reflection(pattern)
        if row_reflection != None:
            print(f"Pattern {idx} had row reflection at {row_reflection}")
            result += row_reflection * 100
            continue
        columns = transpose_list(pattern)
        col_reflection = try_reflection(columns)
        if col_reflection != None:
            print(f"Pattern {idx} had col reflection at {col_reflection}")
            result += col_reflection
            continue
        raise ValueError(f"Pattern {idx} doesnt reflect :(")
    print(result)

def task2(input_lines: list[str]):
    patterns = [[]]
    for line in input_lines:
        if line == "":
            patterns.append([])
        else:
            patterns[-1].append(line)
    print(f"Got {len(patterns)} patterns.")
    result = 0
    for idx, pattern in enumerate(patterns):
        row_reflection = try_second_best_reflection(pattern)
        if row_reflection != None:
            print(f"Pattern {idx} had row reflection at {row_reflection}")
            result += row_reflection * 100
            continue
        columns = transpose_list(pattern)
        col_reflection = try_second_best_reflection(columns)
        if col_reflection != None:
            print(f"Pattern {idx} had col reflection at {col_reflection}")
            result += col_reflection
            continue
        raise ValueError(f"Pattern {idx} doesnt reflect :(")
    print(result)


def transpose_list(input_list: list[str]) -> list[str]:
    result = []
    for line in input_list:
        for idx, char in enumerate(line):
            if len(result) <= idx:
                result.append([])
            result[idx].append(char)
    return result


def try_reflection(columns: list[str]) -> int or None:
    for i in range(1, len(columns)):
        # i is the first column in the right half
        len_left = i
        len_right = len(columns) - len_left
        amount_reflected = min(len_left, len_right)

        matches = True

        for j in range(amount_reflected):
            if columns[i-j-1] != columns[i+j]:
                matches = False
                break
        if matches:
            return i
    return None

def try_second_best_reflection(row_columns: list[str]) -> int or None:
    for i in range(1, len(row_columns)):
        # i is the first column in the right half
        len_left = i
        len_right = len(row_columns) - len_left
        amount_reflected = min(len_left, len_right)

        distance = 0
        for j in range(amount_reflected):
            distance += get_reflection_distance(row_columns[i-j-1], row_columns[i+j])
            if distance > 1:
                break
        print(f"Mirror at {i} has distance {distance}")
        if distance == 1:
            return i
    return None

def get_reflection_distance(left: list[str], right: list[str]) -> int:
    reflection_length = min(len(left), len(right))
    distance = 0
    for i in range(reflection_length):
        if left[i] != right[i]:
            distance += 1
    return distance