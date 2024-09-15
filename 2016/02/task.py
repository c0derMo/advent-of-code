keypad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

def task1(input_lines: list[str]):
    x = 1
    y = 1

    sequence = ""

    for line in input_lines:
        for char in line:
            if char == "U":
                y = max(0, y-1)
            elif char == "D":
                y = min(2, y+1)
            elif char == "L":
                x = max(0, x-1)
            elif char == "R":
                x = min(2, x+1)
        
        sequence += str(keypad[y][x])

    print(sequence)


keypad_2 = [
    [None, None, 1, None, None],
    [None,  2,   3,   4,  None],
    [ 5,    6,   7,   8,    9 ],
    [None, "A", "B", "C", None],
    [None, None, "D", None, None]
]

def task2(input_lines: list[str]):
    x = 0
    y = 3

    sequence = ""

    for line in input_lines:
        for char in line:
            if char == "U" and y > 0 and keypad_2[y-1][x] != None:
                y -= 1
            elif char == "D" and y < 4 and keypad_2[y+1][x] != None:
                y += 1
            elif char == "L" and x > 0 and keypad_2[y][x-1] != None:
                x -= 1
            elif char == "R" and x < 4 and keypad_2[y][x+1] != None:
                x += 1
        #     print(f"Moving to {keypad_2[y][x]}")
        # print(f"Inputting {keypad_2[y][x]}")
        
        sequence += str(keypad_2[y][x])

    print(sequence)