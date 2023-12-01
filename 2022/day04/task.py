import re

def task1(inputLines):
    REGEX = r"(\d+)-(\d+),(\d+)-(\d+)"
    containedLines = 0
    for line in inputLines:
        match = re.search(REGEX, line)
        if not match:
            raise Exception("Invalid line in input")
        e1LowerBound = int(match.group(1))
        e1UpperBound = int(match.group(2))
        e2LowerBound = int(match.group(3))
        e2UpperBound = int(match.group(4))
        # print(f"Line: {line}")
        # print(e1LowerBound)
        # print(e1UpperBound)
        # print(e2LowerBound)
        # print(e2UpperBound)
        if e1LowerBound == e2LowerBound:
            containedLines += 1
            # print("Lower bounds are same")
        elif e1LowerBound < e2LowerBound:
            if e1UpperBound >= e2UpperBound:
                containedLines += 1
                # print("e1 has a lower bound and higher or equal upper bound")
        elif e2LowerBound < e1LowerBound:
            if e2UpperBound >= e1UpperBound:
                containedLines += 1
                # print("e2 has a lower bound and higher or equal upper bound")
    print(f"Dupliacted lines: {containedLines}")

def task2(inputLines):
    REGEX = r"(\d+)-(\d+),(\d+)-(\d+)"
    containedLines = 0
    for line in inputLines:
        match = re.search(REGEX, line)
        if not match:
            raise Exception("Invalid line in input")
        e1LowerBound = int(match.group(1))
        e1UpperBound = int(match.group(2))
        e2LowerBound = int(match.group(3))
        e2UpperBound = int(match.group(4))
        # print(f"Line: {line}")
        # print(e1LowerBound)
        # print(e1UpperBound)
        # print(e2LowerBound)
        # print(e2UpperBound)
        rangeOne = range(e1LowerBound, e1UpperBound+1)
        rangeTwo = range(e2LowerBound, e2UpperBound+1)
        for section in rangeOne:
            if section in rangeTwo:
                containedLines += 1
                break
    print(f"Overlapping lines: {containedLines}")
