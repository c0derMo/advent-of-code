import math

def task1(inputLines):
    xMin, xMax, yMax = findMatrixBounds(inputLines)
    print(f"Our coordinates go from X:{xMin},Y:0 to X:{xMax},Y:{yMax} - List length of {xMax - xMin + 1}/{yMax+1}")
    matrix = buildMatrix(inputLines, xMax - xMin + 1, yMax + 1, xMin)
    # printMatrix(matrix)
    iteration = genSandUntilOutOfBounds(matrix, 500 - xMin, 0, 1)
    print(f"Made it to iteration {iteration}")


def task2(inputLines):
    xMin, xMax, yMax = findMatrixBounds(inputLines)
    print(f"Our coordinates go from X:{xMin},Y:0 to X:{xMax},Y:{yMax} - List length of {xMax - xMin + 1}/{yMax+1}")
    floor = [f"{xMin},{yMax + 2} -> {xMax},{yMax + 2}"]
    matrix = buildMatrix(inputLines + floor, xMax - xMin + 1, yMax + 3, xMin)
    # printMatrix(matrix)
    iteration = 1
    shouldRun = True
    xSpawn = 500 - xMin
    while shouldRun:
        # if iteration % 100 == 0:
        #     print(f"-- Iteration {iteration} -- xSpawn: {xSpawn}")
        shouldRun, matrix, xSpawn = genSandUntilSpawnBlocked(matrix, xSpawn, 0)
        iteration += 1
    print(f"Made it to iteration {iteration - 1}")

def printMatrix(matrix):
    for y in range(len(matrix[0])):
        for x in range(len(matrix)):
            print(matrix[x][y], end="")
        print("")

def findMatrixBounds(lines):
    xMin = int(lines[0].split(" -> ")[0].split(",")[0])
    xMax = int(lines[0].split(" -> ")[0].split(",")[0])
    yMax = int(lines[0].split(" -> ")[0].split(",")[1])

    for line in lines:
        for pair in line.split(" -> "):
            x = int(pair.split(",")[0])
            if x < xMin:
                xMin = x
            if x > xMax:
                xMax = x
            y = int(pair.split(",")[1])
            if y > yMax:
                yMax = y
    return xMin, xMax, yMax

def buildMatrix(lines, xSize, ySize, xOffset):
    matrix = []
    for x in range(xSize):
        col = []
        for y in range(ySize):
            col.append('.')
        matrix.append(col)
    
    for line in lines:
        pairs = line.split(" -> ")
        i = 1
        while i < len(pairs):
            old = pairs[i-1].split(",")
            new = pairs[i].split(",")

            xOld = int(old[0]) - xOffset
            yOld = int(old[1])
            xNew = int(new[0]) - xOffset
            yNew = int(new[1])

            matrix[xOld][yOld] = "#"
            matrix[xNew][yNew] = "#"
            while xOld < xNew:
                xOld += 1
                matrix[xOld][yOld] = "#"
            while xOld > xNew:
                xOld -= 1
                matrix[xOld][yOld] = "#"
            while yOld < yNew:
                yOld += 1
                matrix[xOld][yOld] = "#"
            while yOld > yNew:
                yOld -= 1
                matrix[xOld][yOld] = "#"

            i += 1
    return matrix

def genSandUntilOutOfBounds(matrix, xSpawn, ySpawn, iteration):
    xSand = xSpawn
    ySand = ySpawn

    yMax = len(matrix[0])

    running = True
    while running:
        # Checking flow out the bottom
        if ySand >= yMax - 1:
            return iteration - 1
        # Checking directly beneath
        elif matrix[xSand][ySand + 1] == ".":
            ySand += 1
        # Checking flow out the sides
        elif xSand <= 0 or xSand >= len(matrix) - 1:
            return iteration - 1
        # Checking diagonally left
        elif matrix[xSand - 1][ySand + 1] == ".":
            ySand += 1
            xSand -= 1
        # Checking diagonally right
        elif matrix[xSand + 1][ySand + 1] == ".":
            ySand += 1
            xSand += 1
        # Not oob and can't flow anymore
        else:
            running = False
    matrix[xSand][ySand] = "o"
    # print(f"--- [ITERATION {iteration}] ---")
    # printMatrix(matrix)
    return genSandUntilOutOfBounds(matrix, xSpawn, ySpawn, iteration + 1)

def genSandUntilSpawnBlocked(matrix, xSpawn, ySpawn):
    if matrix[xSpawn][ySpawn] != ".":
        return False, matrix, xSpawn
    
    xSand = xSpawn
    ySand = ySpawn

    yMax = len(matrix[0])

    running = True
    while running:
        # Checking flow out the bottom - impossible now
        if ySand >= yMax - 1:
            raise ValueError(f"Iteration flew out the bottom")
        # Checking directly beneath
        elif matrix[xSand][ySand + 1] == ".":
            ySand += 1
        # Checking flow out the sides - adding more columns
        elif xSand <= 0:
            newLine = []
            for y in range(yMax - 1):
                newLine.append(".")
            newLine.append("#")
            matrix.insert(0, newLine)
            xSand += 1
            xSpawn += 1
            # print("Added column on the left, shifted xSpawn")
        elif xSand >= len(matrix) - 1:
            newLine = []
            for y in range(yMax - 1):
                newLine.append(".")
            newLine.append("#")
            matrix.append(newLine)
        # Checking diagonally left
        elif matrix[xSand - 1][ySand + 1] == ".":
            ySand += 1
            xSand -= 1
        # Checking diagonally right
        elif matrix[xSand + 1][ySand + 1] == ".":
            ySand += 1
            xSand += 1
        # Not oob and can't flow anymore
        else:
            running = False
    matrix[xSand][ySand] = "o"
    # print(f"--- [ITERATION {iteration}] ---")
    # printMatrix(matrix)
    # return genSandUntilSpawnBlocked(matrix, xSpawn, ySpawn, iteration + 1) - Can't do this recursive like this, max recursion depth lol
    return True, matrix, xSpawn