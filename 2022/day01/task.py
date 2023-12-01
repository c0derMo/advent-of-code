def task1(inputLines):
    elves = [0]
    current_elf = 0

    for line in inputLines:
        if line == "":
            elves.append(0)
            current_elf += 1
        else:
            elves[current_elf] += int(line)
    print(f"Max: {max(elves)}")

def task2(inputLines):
    elves = [0]
    current_elf = 0

    for line in inputLines:
        if line == "":
            elves.append(0)
            current_elf += 1
        else:
            elves[current_elf] += int(line)
    
    total_max = 0
    for i in range(0,3):
        max_cal = max(elves)
        print(f"Max: {max_cal}")
        total_max += max_cal
        elves.remove(max_cal)
    print(f"Total max: {total_max}")
