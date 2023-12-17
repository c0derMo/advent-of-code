def task1(input_lines: list[str]):
    energized_tiles = get_energized_tiles(input_lines)

    energized_tiles_count = 0
    for col in energized_tiles:
        for tile in col:
            if tile["l"] or tile["d"] or tile["u"] or tile["r"]:
                energized_tiles_count += 1
    print(energized_tiles_count)

def task2(input_lines: list[str]):
    max_energized = 0

    for y in range(len(input_lines)):
        tiles = get_energized_tiles(input_lines, starting_tiles=[(0,y,"r")])
        energized_tiles_count = 0
        for col in tiles:
            for tile in col:
                if tile["l"] or tile["d"] or tile["u"] or tile["r"]:
                    energized_tiles_count += 1
        if energized_tiles_count > max_energized:
            max_energized = energized_tiles_count
    print("Left done")
    
    for y in range(len(input_lines)):
        tiles = get_energized_tiles(input_lines, starting_tiles=[(len(input_lines[0])-1,y,"l")])
        energized_tiles_count = 0
        for col in tiles:
            for tile in col:
                if tile["l"] or tile["d"] or tile["u"] or tile["r"]:
                    energized_tiles_count += 1
        if energized_tiles_count > max_energized:
            max_energized = energized_tiles_count
    print("Right done")

    for x in range(len(input_lines[0])):
        tiles = get_energized_tiles(input_lines, starting_tiles=[(x,0,"d")])
        energized_tiles_count = 0
        for col in tiles:
            for tile in col:
                if tile["l"] or tile["d"] or tile["u"] or tile["r"]:
                    energized_tiles_count += 1
        if energized_tiles_count > max_energized:
            max_energized = energized_tiles_count
    print("Up done")
    
    for x in range(len(input_lines[0])):
        tiles = get_energized_tiles(input_lines, starting_tiles=[(x,len(input_lines)-1,"u")])
        energized_tiles_count = 0
        for col in tiles:
            for tile in col:
                if tile["l"] or tile["d"] or tile["u"] or tile["r"]:
                    energized_tiles_count += 1
        if energized_tiles_count > max_energized:
            max_energized = energized_tiles_count
    print("Down done")
    
    print(max_energized)


def get_energized_tiles(tiles: list[str], starting_tiles=[(0,0,"r")]) -> list[list[dict[str, bool]]]:
    y_max = len(tiles)
    x_max = len(tiles[0])
    energized_tiles: list[list[dict[str, bool]]] = []
    for x in range(x_max):
        col = []
        for y in range(y_max):
            col.append({"l": False, "r": False, "u": False, "d": False})
        energized_tiles.append(col)
    
    queue = starting_tiles
    while len(queue) > 0:
        x, y, direction = queue.pop(0)
        if x >= x_max or x < 0 or y >= y_max or y < 0:
            continue
        if energized_tiles[x][y][direction]:
            continue
        energized_tiles[x][y][direction] = True

        if tiles[y][x] == ".":
            if direction == "r":
                queue.append((x+1,y,"r"))
            elif direction == "l":
                queue.append((x-1,y,"l"))
            elif direction == "u":
                queue.append((x,y-1,"u"))
            elif direction == "d":
                queue.append((x,y+1,"d"))
        elif tiles[y][x] == "-":
            if direction == "r":
                queue.append((x+1,y,"r"))
            elif direction == "l":
                queue.append((x-1,y,"l"))
            elif direction == "u" or direction == "d":
                queue.append((x+1,y,"r"))
                queue.append((x-1,y,"l"))
        elif tiles[y][x] == "|":
            if direction == "r" or direction == "l":
                queue.append((x,y-1,"u"))
                queue.append((x,y+1,"d"))
            elif direction == "u":
                queue.append((x,y-1,"u"))
            elif direction == "d":
                queue.append((x,y+1,"d"))
        elif tiles[y][x] == "\\":
            if direction == "r":
                queue.append((x,y+1,"d"))
            elif direction == "l":
                queue.append((x,y-1,"u"))
            elif direction == "u":
                queue.append((x-1,y,"l"))
            elif direction == "d":
                queue.append((x+1,y,"r"))
        elif tiles[y][x] == "/":
            if direction == "r":
                queue.append((x,y-1,"u"))
            elif direction == "l":
                queue.append((x,y+1,"d"))
            elif direction == "u":
                queue.append((x+1,y,"r"))
            elif direction == "d":
                queue.append((x-1,y,"l"))
    
    return energized_tiles