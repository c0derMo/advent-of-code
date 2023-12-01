def task1(inputLines):
    cycle = 0
    register = 1
    resultStrength = 0
    for line in inputLines:
        if line == "noop":
            cycle += 1
            resultStrength += checkCycle(cycle, register)
        if line.startswith("addx"):
            cycle += 1
            resultStrength += checkCycle(cycle, register)
            cycle += 1
            resultStrength += checkCycle(cycle, register)
            register += int(line.split(" ")[1])
    print(f"Result: {resultStrength}")

def task2(inputLines):
    cycle = 0
    register = 1
    resultStrength = 0
    for line in inputLines:
        if line == "noop":
            drawCRT(cycle, register)
            cycle += 1
            resultStrength += checkCycle(cycle, register, True)
        if line.startswith("addx"):
            drawCRT(cycle, register)
            cycle += 1
            resultStrength += checkCycle(cycle, register, True)
            drawCRT(cycle, register)
            cycle += 1
            resultStrength += checkCycle(cycle, register, True)
            register += int(line.split(" ")[1])

def drawCRT(cycle: int, register: int):
    modCycle = cycle % 40
    if abs(register - modCycle) <= 1:
        print("#", end="")
    else:
        print(".", end="")
    if modCycle == 39:
        print("")

def checkCycle(cycle: int, register: int, mute: bool=False):
    if cycle in [20, 60, 100, 140, 180, 220]:
        if not mute:
            print(f"Signal strength at cycle {cycle}: {register}")
        return cycle * register
    return 0