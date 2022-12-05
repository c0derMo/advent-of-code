import math
import re

def task1(inputLines):
    stacks = [[]]

    # Calculating amount of stacks
    amStacks = math.ceil(len(inputLines[0]) / 4)
    for i in range(0, amStacks+1):
        stacks.append([])

    buildingStacks = True

    for line in inputLines:
        if line == "":
            buildingStacks = False
            for idx in range(0, len(stacks)):
                stacks[idx].reverse()
            continue
        if buildingStacks:
            i = 0
            idx = 1
            while i < len(line):
                match = re.match(r"^\[(\w)\]$", line[i:i+3])
                if match:
                    stacks[idx].append(match.group(1))
                i += 4
                idx += 1
        else:
            match = re.match(r"move (\d+) from (\d+) to (\d+)", line)
            if not match:
                raise Exception("Invalid input line: " + line)
            # print(line)
            amountCrates = int(match.group(1))
            start = int(match.group(2))
            target = int(match.group(3))
            # print(f"Moving {amountCrates} from {start} to {target}")
            for i in range(0, amountCrates):
                crate = stacks[start].pop()
                # print(f"Moving {crate} from {start} to {target}")
                stacks[target].append(crate)
                # print(stacks)
    # print(stacks)
    result = ""
    for stack in stacks:
        if len(stack) > 0:
            result += stack.pop()
    print(result)

def task2(inputLines):
    stacks = [[]]

    # Calculating amount of stacks
    amStacks = math.ceil(len(inputLines[0]) / 4)
    for i in range(0, amStacks+1):
        stacks.append([])

    buildingStacks = True

    for line in inputLines:
        if line == "":
            buildingStacks = False
            for idx in range(0, len(stacks)):
                stacks[idx].reverse()
            continue
        if buildingStacks:
            i = 0
            idx = 1
            while i < len(line):
                match = re.match(r"^\[(\w)\]$", line[i:i+3])
                if match:
                    stacks[idx].append(match.group(1))
                i += 4
                idx += 1
        else:
            match = re.match(r"move (\d+) from (\d+) to (\d+)", line)
            if not match:
                raise Exception("Invalid input line: " + line)
            # print(line)
            amountCrates = int(match.group(1))
            start = int(match.group(2))
            target = int(match.group(3))
            # print(f"Moving {amountCrates} from {start} to {target}")
            cratesToMove = []
            for i in range(0, amountCrates):
                cratesToMove.append(stacks[start].pop())
                # print(f"Moving {crate} from {start} to {target}")
            cratesToMove.reverse()
            for crate in cratesToMove:
                stacks[target].append(crate)
                # print(stacks)
    # print(stacks)
    result = ""
    for stack in stacks:
        if len(stack) > 0:
            result += stack.pop()
    print(result)