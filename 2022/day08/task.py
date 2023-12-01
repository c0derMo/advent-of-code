def task1(inputLines):
    matrix = inputToMatrix(inputLines)

    tallestTrees = []
    dimY = len(matrix)
    dimX = len(matrix[0])

    # Rows
    for i in range(dimY):
        maxHeight = -1
        for j in range(dimX):
            if int(matrix[i][j]) > maxHeight:
                maxHeight = int(matrix[i][j])
                if (i, j) not in tallestTrees:
                    tallestTrees.append((i, j))
        maxHeight = -1
        for j in range(dimX-1, -1, -1):
            if int(matrix[i][j]) > maxHeight:
                maxHeight = int(matrix[i][j])
                if (i, j) not in tallestTrees:
                    tallestTrees.append((i, j))
    
    # Column
    for j in range(dimX):
        maxHeight = -1
        for i in range(dimY):
            if int(matrix[i][j]) > maxHeight:
                maxHeight = int(matrix[i][j])
                if (i, j) not in tallestTrees:
                    tallestTrees.append((i, j))
        maxHeight = -1
        for i in range(dimY-1, -1, -1):
            if int(matrix[i][j]) > maxHeight:
                maxHeight = int(matrix[i][j])
                if (i, j) not in tallestTrees:
                    tallestTrees.append((i, j))

    print(tallestTrees)
    print(len(tallestTrees))

def task2(inputLines):
    matrix = inputToMatrix(inputLines)

    # print(matrix)

    dimY = len(matrix)
    dimX = len(matrix[0])

    highestScore = 0
    # print(getScenicScore(matrix, 2, 1))
    for row in range(dimX):
        for col in range(dimY):
            score = getScenicScore(matrix, row, col)
            # print(f"Scenic score of {row}{col}: {score}")
            if score > highestScore:
                highestScore = score

    print(highestScore)

def inputToMatrix(lines: [str]) -> [[int]]:
    result = []
    for rowStr in lines:
        row = []
        for s in list(rowStr):
            row.append(int(s))
        result.append(row)
    return result

def getScenicScore(matrix: [[int]], x: int, y: int):
    dimY = len(matrix)
    dimX = len(matrix[0])

    finalScore = 0
    # Walking up
    i = y
    while i > 0:
        i -= 1
        if i <= 0 or not matrix[i][x] < matrix[y][x]:
            break
    walkedDistance = abs(y - i)
    finalScore = walkedDistance

    # Walking down
    i = y
    while i < dimY-1:
        i += 1
        if i >= dimY-1 or not matrix[i][x] < matrix[y][x]:
            break
    walkedDistance = abs(i - y)
    finalScore *= walkedDistance

    # Walking left
    i = x
    while i > 0:
        i -= 1
        if i <= 0 or not matrix[y][i] < matrix[y][x]:
            break
    walkedDistance = abs(x - i)
    finalScore *= walkedDistance

    # Walking right
    i = x
    while i < dimX-1:
        i += 1
        if i >= dimX-1 or not matrix[y][i] < matrix[y][x]:
            break
    walkedDistance = abs(i - x)
    finalScore *= walkedDistance

    return finalScore
