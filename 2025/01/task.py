MAX_NUM = 99

def task1(input_lines: list[str]):
    state = 50

    zeros = 0

    for line in input_lines:
        if line.startswith("L"):
            state -= int(line[1:])
        elif line.startswith("R"):
            state += int(line[1:])
        else:
            raise AttributeError("Line doesnt start with L or R")
        state %= MAX_NUM+1
        if state == 0:
            zeros += 1
        print(state)
    
    print(zeros)

def task2(input_lines: list[str]):
    state = 50
    zeros = 0

    for line in input_lines:
        change = int(line[1:])

        while change > MAX_NUM:
            change -= MAX_NUM+1
            zeros += 1
        
        if line.startswith("L"):
            change = -change
        
        if state + change > MAX_NUM:
            zeros += 1
        if state + change < 0 and state != 0:
            zeros += 1

        state += change

        if state == 0:
            zeros += 1

        state %= MAX_NUM+1

        #print(f"{line}: {state} {zeros}")
    
    print(zeros)