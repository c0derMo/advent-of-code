def task1(input_lines: list[str]):
    count = search_horizontal(input_lines)
    print(count)
    count += search_vertical(input_lines)
    print(count)
    count += search_diag_tl_br(input_lines)
    print(count)
    count += search_diag_tr_bl(input_lines)
    print(count)

def task2(input_lines: list[str]):
    total_count = 0
    patterns = [
        ["M.S",
         ".A.",
         "M.S"],
        ["M.M",
         ".A.",
         "S.S"],
        ["S.S",
         ".A.",
         "M.M"],
        ["S.M",
         ".A.",
         "S.M"],
    ]
    for pattern in patterns:
        total_count += count_pattern_in_grid(input_lines, pattern)

    print(total_count)

def search_horizontal(board: list[str]):
    count = 0
    for row in board:
        count += xmas_occurances(row)
    return count

def search_vertical(board: list[str]):
    count = 0
    for col_idx in range(len(board[0])):
        col = ''.join([board[i][col_idx] for i in range(len(board))])
        count += xmas_occurances(col)
    return count

def search_diag_tl_br(board: list[str]):
    count = 0
    for diag_idx in range(1, len(board[0])):
        upper_diag = ''.join([board[i][i + diag_idx] for i in range(len(board[0]) - diag_idx)])
        lower_diag = ''.join([board[i + diag_idx][i] for i in range(len(board[0]) - diag_idx)])
        count += xmas_occurances(upper_diag)
        count += xmas_occurances(lower_diag)
    middle_diag = ''.join([board[i][i] for i in range(len(board[0]))])
    count += xmas_occurances(middle_diag)
    return count

def search_diag_tr_bl(board: list[str]):
    count = 0
    for diag_idx in range(1, len(board[0])):
        upper_diag = ''.join([board[i][len(board[0]) - i - diag_idx - 1] for i in range(len(board[0]) - diag_idx)])
        lower_diag = ''.join([board[i + diag_idx][len(board[0]) - i - 1] for i in range(len(board[0]) - diag_idx)])
        count += xmas_occurances(upper_diag)
        count += xmas_occurances(lower_diag)
    middle_diag = ''.join([board[i][len(board[0]) - 1 - i] for i in range(len(board[0]))])
    count += xmas_occurances(middle_diag)
    return count

def xmas_occurances(line: str) -> int:
    count = 0
    if line.startswith("XMAS"):
        count += 1
    if line.endswith("SAMX"):
        count += 1
    for offset in range(1, len(line)):
        if line[offset:].startswith("XMAS"):
            count += 1
        if line[:-offset].endswith("SAMX"):
            count += 1
    return count

def count_pattern_in_grid(grid: list[str], pattern: list[str], wildcard_char=".") -> int:
    count = 0
    for y in range(len(grid) - len(pattern) + 1):
        for x in range(len(grid[0]) - len(pattern[0]) + 1):
            sub_grid = [r[x:x+len(pattern[0])] for r in grid[y:y+len(pattern)]]
            # print(sub_grid)
            if is_pattern(sub_grid, pattern, wildcard_char):
                count += 1
    return count

def is_pattern(grid: list[str], pattern: list[str], wildcard_char=".") -> bool:
    if len(grid) != len(pattern) or len(grid[0]) != len(pattern[0]):
        raise ValueError("can only compare square patterns")
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if pattern[y][x] != wildcard_char and pattern[y][x] != grid[y][x]:
                return False
    return True