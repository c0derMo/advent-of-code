def task1(input_lines: list[str]):
    start = input_lines[0]

    for i in range(40):
        # print(start)
        print(i)
        start = forwards(start)

    # print(start)
    print(len(start))

def task2(input_lines: list[str]):
    start = input_lines[0]

    for i in range(50):
        print(i)
        start = forwards(start)

    print(len(start))

def forwards(number: str) -> str:
    last_num = ""
    counter = 0
    result = ""

    for char in number:
        if len(last_num) == 0 or last_num == char:
            counter += 1
        else:
            result += str(counter) + last_num
            counter = 1
        last_num = char
    
    result += str(counter) + last_num

    return result