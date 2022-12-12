def task1(inputLines):
    matrix, yStart, xStart, yEnd, xEnd = linesToMatrix(inputLines)
    print(matrix)
    print(xStart)
    print(yStart)
    print(xEnd)
    print(yEnd)
    length = recursiveFindPathLength(matrix, [(xEnd, yEnd)], [], [(xStart, yStart)], 0)
    print(length)

def task2(inputLines):
    matrix, yStart, xStart, yEnd, xEnd = linesToMatrix(inputLines)
    allStarts = []
    for idy, row in enumerate(matrix):
        for idx, f in enumerate(row):
            if f == 0:
                allStarts.append((idy, idx))
    print(allStarts)
    length = recursiveFindPathLength(matrix, [(xEnd, yEnd)], [], allStarts, 0)
    print(length)

def recursiveFindPathLength(matrix, currentNodes, previousNodes, target, iteration):
    totalNodes = len(matrix) * len(matrix[0])
    print(f"Iteration {iteration} - Total Nodes: {totalNodes}; Visited Nodes: {len(previousNodes)}; Nodes checking this iteration: {len(currentNodes)} - Nodes remaining untouched: {totalNodes - len(previousNodes)}")
    if len(currentNodes) == 0:
        raise ValueError("No current nodes were given")
    if target in previousNodes:
        raise ValueError(f"Somehow, target node {node} made it's way into the previousNodes set in interation {iteration}")
    intersection = [value for value in previousNodes if value in currentNodes]
    if len(intersection) > 0:
        raise ValueError(f"Somehow, we have {len(intersection)} similar elements in currentNodes and previousNodes")
    newNodes = []
    for node in currentNodes:
        if node == target:
            raise ValueError(f"Somehow, target node {node} made it's way into the currentNode set in interation {iteration}")
        # print(node)
        # print(matrix[node[0]][node[1]])
        # print(matrix[node[0]+1][node[1]])
        # print(matrix[node[0]-1][node[1]])
        # print(matrix[node[0]][node[1]+1])
        # print(matrix[node[0]][node[1]-1])
        # We try to walk in all 4 directions to see if we can make progress
        if node[0] > 0 and matrix[node[0]-1][node[1]] - matrix[node[0]][node[1]] >= -1:
            # Walking up
            # print("Walking up")
            newNode = (node[0]-1, node[1])
            if newNode not in previousNodes:
                if newNode in target:
                    return iteration + 1
                if newNode not in newNodes:
                    newNodes.append(newNode)
        if node[0] < len(matrix)-1 and matrix[node[0]+1][node[1]] - matrix[node[0]][node[1]] >= -1:
            # Walking down
            # print("Walking down")
            newNode = (node[0]+1, node[1])
            if newNode not in previousNodes:
                if newNode in target:
                    return iteration + 1
                if newNode not in newNodes:
                    newNodes.append(newNode)
        if node[1] > 0 and matrix[node[0]][node[1]-1] - matrix[node[0]][node[1]] >= -1:
            # Walking left
            # print("Walking left")
            newNode = (node[0], node[1]-1)
            if newNode not in previousNodes:
                if newNode in target:
                    return iteration + 1
                if newNode not in newNodes:
                    newNodes.append(newNode)
        if node[1] < len(matrix[0])-1 and matrix[node[0]][node[1]+1] - matrix[node[0]][node[1]] >= -1:
            # Walking right
            # print("Walking right")
            newNode = (node[0], node[1]+1)
            if newNode not in previousNodes:
                if newNode in target:
                    return iteration + 1
                if newNode not in newNodes:
                    newNodes.append(newNode)
    
    # print(newNodes)
    # print(previousNodes + currentNodes)
    return recursiveFindPathLength(matrix, newNodes, previousNodes + currentNodes, target, iteration + 1)

def linesToMatrix(inputLines):
    result = []
    xStart = 0
    yStart = 0
    xEnd = 0
    yEnd = 0
    for idy, line in enumerate(inputLines):
        row = []
        for idx, char in enumerate(line):
            if char == "S":
                height = 0
                xStart = idx
                yStart = idy
            elif char == "E":
                height = 25
                xEnd = idx
                yEnd = idy
            else:
                height = ord(char) - 97
            row.append(height)
        result.append(row)
    return result, xStart, yStart, xEnd, yEnd