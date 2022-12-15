import re
from itertools import permutations

REGEX_SENSOR = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"

def task1(inputLines):
    sensors = parseSensors(inputLines)
    # print(sensors)

    yToLookAt = 2000000
    # yToLookAt = 10

    print("Starting direction 1")
    # Direction 1
    x = sensors[0]['sensor'][0]
    impossibleSpaces = []
    distanceDecreasing = False
    while not distanceDecreasing:
        if x % 10000 == 0:
            print(f"Dir1 loop - {x}")
        covered = False
        for sensor in sensors:
            if manhattanDistance((x, yToLookAt), sensor['sensor']) <= sensor['distance']:
                covered = True
                impossibleSpaces.append((x, yToLookAt))
                break
        if not covered:
            distanceDecreasing = True
            for sensor in sensors:
                if manhattanDistance((x, yToLookAt), sensor['sensor']) <= manhattanDistance((x - 1, yToLookAt), sensor['sensor']):
                    distanceDecreasing = False
                    break
        x += 1

    print("Starting direction 2")
    # Direction 2
    x = sensors[0]['sensor'][0]
    distanceDecreasing = False
    while not distanceDecreasing:
        if x % 10000 == 0:
            print(f"Dir2 loop - {x}")
        covered = False
        for sensor in sensors:
            if manhattanDistance((x, yToLookAt), sensor['sensor']) <= sensor['distance']:
                covered = True
                impossibleSpaces.append((x, yToLookAt))
                break
        if not covered:
            distanceDecreasing = True
            for sensor in sensors:
                if manhattanDistance((x, yToLookAt), sensor['sensor']) <= manhattanDistance((x + 1, yToLookAt), sensor['sensor']):
                    distanceDecreasing = False
                    break
        x -= 1

    amountSpaces = len(impossibleSpaces)
    # print(amountSpaces)
    print("Removing beacons from impossibleSpaces")
    # Removing beacons from the result
    for sensor in sensors:
        if sensor['beacon'][1] == yToLookAt:
            amountSpaces -= 1

    print(amountSpaces + 1)
    # print("Unimplemented")

def task2(inputLines):
    sensors = parseSensors(inputLines)
    # print(sensors)

    lines1 = []
    lines2 = []

    for sensor in sensors:
        line1_1 = sensor['sensor'][1] + sensor['sensor'][0] - sensor['distance']
        line1_2 = sensor['sensor'][1] + sensor['sensor'][0] + sensor['distance']
        line2_1 = sensor['sensor'][1] - sensor['sensor'][0] - sensor['distance']
        line2_2 = sensor['sensor'][1] - sensor['sensor'][0] + sensor['distance']
        lines1.append(line1_1)
        lines1.append(line1_2)
        lines2.append(line2_1)
        lines2.append(line2_2)
    
    line1Pairs = []
    line2Pairs = []

    for line1 in lines1:
        for line2 in lines1:
            if line1 - line2 == 2:
                # print(f"{line1} - {line2}")
                line1Pairs.append((line1, line2))
            if line1 - line2 == -2:
                line1Pairs.append((line2, line1))
    for line1 in lines2:
        for line2 in lines2:
            if line1 - line2 == 2:
                # print(f"{line1} - {line2}")
                line2Pairs.append((line1, line2))
            if line1 - line2 == -2:
                line2Pairs.append((line2, line1))

    print(len(line1Pairs))
    print(len(line2Pairs))

    size = 4000000

    for pair1 in line1Pairs:
        for pair2 in line2Pairs:
            # pair1[0] - x == pair2[0] + x
            x = (pair1[0] - pair2[0]) / 2
            y = pair1[0] - x - 1
            if x > size or x < 0 or y > size or y < 0:
                continue
            covered = False
            for sensor in sensors:
                if manhattanDistance((x,y), sensor['sensor']) <= sensor['distance']:
                    covered = True
                    break
            if not covered:
                # We may have found the thing
                print(f"{x} - {y} - ({x * 4000000 + y})")

def manhattanDistance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def parseSensors(lines):
    result = []
    for line in lines:
        match = re.match(REGEX_SENSOR, line)
        if not match:
            raise ValueError(f"Line '{line}' didn't match regex")
        sensor = {
            "sensor": (int(match.group(1)), int(match.group(2))),
            "beacon": (int(match.group(3)), int(match.group(4))),
            "distance": -1
        }
        sensor['distance'] = manhattanDistance(sensor['sensor'], sensor['beacon'])
        result.append(sensor)
    return result