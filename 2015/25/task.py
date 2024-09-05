def task1(input_lines: list[str]):
    row = 1
    col = 1
    num = 20151125

    target_row = 2947
    target_col = 3029

    while row != target_row or col != target_col:
        num = calculate_next_number(num)
        if row > 1:
            row -= 1
            col += 1
        else:
            row = col + 1
            col = 1

    print(num)

def task2(input_lines: list[str]):
    print("Unimplemented")


def calculate_next_number(prev_number: int) -> int:
    return (prev_number * 252533) % 33554393