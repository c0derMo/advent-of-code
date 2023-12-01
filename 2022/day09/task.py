def task1(inputLines):
    currentHead = [0,0]
    currentTail = [0,0]

    visitedSpaces = []

    for line in inputLines:
        lineSplit = line.split(" ")
        distance = int(lineSplit[1])
        # print(f"{lineSplit[0]} - Distance {distance}")
        for i in range(distance):
            if lineSplit[0] == "D":
                currentHead[1] -= 1
            elif lineSplit[0] == "U":
                currentHead[1] += 1
            elif lineSplit[0] == "L":
                currentHead[0] -= 1
            elif lineSplit[0] == "R":
                currentHead[0] += 1
            else:
                raise ValueError(f"Unknown direction {lineSplit[0]}")
            currentTail = updateTail(currentHead, currentTail)
            # print(f"Head at {currentHead}, tail at {currentTail}")
            if tuple(currentTail) not in visitedSpaces:
                visitedSpaces.append(tuple(currentTail))
    print(len(visitedSpaces))

def task2(inputLines):
    ropeNodes = [
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0]
    ]
    visitedSpaces = []

    for line in inputLines:
        lineSplit = line.split(" ")
        distance = int(lineSplit[1])
        # print(f"{lineSplit[0]} - Distance {distance}")
        for i in range(distance):
            if lineSplit[0] == "D":
                ropeNodes[0][1] -= 1
            elif lineSplit[0] == "U":
                ropeNodes[0][1] += 1
            elif lineSplit[0] == "L":
                ropeNodes[0][0] -= 1
            elif lineSplit[0] == "R":
                ropeNodes[0][0] += 1
            else:
                raise ValueError(f"Unknown direction {lineSplit[0]}")
            ropeNodes[1] = updateTail(ropeNodes[0], ropeNodes[1])
            ropeNodes[2] = updateTail(ropeNodes[1], ropeNodes[2])
            ropeNodes[3] = updateTail(ropeNodes[2], ropeNodes[3])
            ropeNodes[4] = updateTail(ropeNodes[3], ropeNodes[4])
            ropeNodes[5] = updateTail(ropeNodes[4], ropeNodes[5])
            ropeNodes[6] = updateTail(ropeNodes[5], ropeNodes[6])
            ropeNodes[7] = updateTail(ropeNodes[6], ropeNodes[7])
            ropeNodes[8] = updateTail(ropeNodes[7], ropeNodes[8])
            ropeNodes[9] = updateTail(ropeNodes[8], ropeNodes[9])
            # print(f"Head at {currentHead}, tail at {currentTail}")
            if tuple(ropeNodes[9]) not in visitedSpaces:
                visitedSpaces.append(tuple(ropeNodes[9]))
    print(len(visitedSpaces))

def updateTail(head, tail):
    xDiff = head[0] - tail[0]
    yDiff = head[1] - tail[1]
    currentTail = tail
    if abs(xDiff) > 1 or abs(yDiff) > 1:
        if head[0] != tail[0] and head[1] != tail[1]:
            # Diagonal motion
            if xDiff >= 1:
                currentTail[0] += 1
            if xDiff <= -1:
                currentTail[0] -= 1
            if yDiff >= 1:
                currentTail[1] += 1
            if yDiff <= -1:
                currentTail[1] -= 1
        elif xDiff > 1:
            # Not adjacent anymore
            currentTail[0] += 1
        elif xDiff < -1:
            currentTail[0] -= 1
        elif yDiff > 1:
            currentTail[1] += 1
        elif yDiff < -1:
            currentTail[1] -= 1
    return currentTail