def task1(input_lines: list[str]):
    # Stupid implementation that uses a 1000x1000 array
    lamps = [[False for _ in range(1000)] for _ in range(1000)]
    
    for line in input_lines:
        if line.startswith("turn on"):
            without_instruct = line[8:]
            pairs = without_instruct.split(" through ")
            start_coords = pairs[0].split(",")
            end_coords = pairs[1].split(",")
            for x in range(int(start_coords[0]), int(end_coords[0])+1):
                for y in range(int(start_coords[1]), int(end_coords[1])+1):
                    lamps[x][y] = True
        elif line.startswith("turn off"):
            without_instruct = line[9:]
            pairs = without_instruct.split(" through ")
            start_coords = pairs[0].split(",")
            end_coords = pairs[1].split(",")
            for x in range(int(start_coords[0]), int(end_coords[0])+1):
                for y in range(int(start_coords[1]), int(end_coords[1])+1):
                    lamps[x][y] = False
        elif line.startswith("toggle"):
            without_instruct = line[7:]
            pairs = without_instruct.split(" through ")
            start_coords = pairs[0].split(",")
            end_coords = pairs[1].split(",")
            for x in range(int(start_coords[0]), int(end_coords[0])+1):
                for y in range(int(start_coords[1]), int(end_coords[1])+1):
                    lamps[x][y] = not lamps[x][y]
        else:
            print(f"Unknown instruction: {line}")
    
    amount = 0
    for row in lamps:
        for lamp in row:
            if lamp:
                amount += 1
    print(amount)

def task2(input_lines: list[str]):
    # Stupid implementation that uses a 1000x1000 array
    lamps = [[0 for _ in range(1000)] for _ in range(1000)]
    
    for line in input_lines:
        if line.startswith("turn on"):
            without_instruct = line[8:]
            pairs = without_instruct.split(" through ")
            start_coords = pairs[0].split(",")
            end_coords = pairs[1].split(",")
            for x in range(int(start_coords[0]), int(end_coords[0])+1):
                for y in range(int(start_coords[1]), int(end_coords[1])+1):
                    lamps[x][y] += 1
        elif line.startswith("turn off"):
            without_instruct = line[9:]
            pairs = without_instruct.split(" through ")
            start_coords = pairs[0].split(",")
            end_coords = pairs[1].split(",")
            for x in range(int(start_coords[0]), int(end_coords[0])+1):
                for y in range(int(start_coords[1]), int(end_coords[1])+1):
                    lamps[x][y] = max(0, lamps[x][y]-1)
        elif line.startswith("toggle"):
            without_instruct = line[7:]
            pairs = without_instruct.split(" through ")
            start_coords = pairs[0].split(",")
            end_coords = pairs[1].split(",")
            for x in range(int(start_coords[0]), int(end_coords[0])+1):
                for y in range(int(start_coords[1]), int(end_coords[1])+1):
                    lamps[x][y] += 2
        else:
            print(f"Unknown instruction: {line}")
    
    amount = 0
    for row in lamps:
        for lamp in row:
            amount += lamp
    print(amount)