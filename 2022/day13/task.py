import re
from math import ceil
import functools

REGEX_LIST = r"^\[(.*)\]$"

def task1(inputLines):
    pair = 1
    result = 0
    for i in range(0, len(inputLines), 3):
        cmp = recursiveCompare(inputLines[i], inputLines[i+1])
        if cmp < 0:
            # print("Correct order")
            result += pair
        if cmp > 0:
            # print("Incorrect order")
            pass
        if cmp == 0:
            print(f"Pair {pair} = 0?")
        pair += 1
    print(result)

def task2(inputLines):
    modLines = []
    for line in inputLines:
        if line != "":
            modLines.append(line)
    modLines.append("[[2]]")
    modLines.append("[[6]]")
    print(f"Amount of packets: {len(modLines)}")
    sortedLines = sorted(modLines, key=functools.cmp_to_key(recursiveCompare))
    p1 = 0
    p2 = 0
    for idx, line in enumerate(sortedLines):
        if line == "[[2]]":
            p1 = idx+1
        if line == "[[6]]":
            p2 = idx+1
    print(p1 * p2)


def recursiveCompare(left: str, right: str) -> int:
    isLeftList = False
    isRightList = False
    if re.match(REGEX_LIST, left):
        isLeftList = True
        left = re.match(REGEX_LIST, left).group(1)
    if re.match(REGEX_LIST, right):
        isRightList = True
        right = re.match(REGEX_LIST, right).group(1)
    # print(f"Comparing {left} {right}")
    if isLeftList == False and isRightList == False:
        # Both are ints
        return int(left) - int(right)
    else:
        # At least one is a list
        leftIdx = 0
        rightIdx = 0
        leftItem = ""
        rightItem = ""
        leftOpenBrackets = 0
        rightOpenBrackets = 0
        while leftIdx < len(left) and rightIdx < len(right):
            while leftIdx < len(left) and (left[leftIdx] != "," or leftOpenBrackets != 0):
                leftItem += left[leftIdx]
                if left[leftIdx] == "[":
                    leftOpenBrackets += 1
                elif left[leftIdx] == "]":
                    leftOpenBrackets -= 1
                leftIdx += 1
            while rightIdx < len(right) and (right[rightIdx] != "," or rightOpenBrackets != 0):
                rightItem += right[rightIdx]
                if right[rightIdx] == "[":
                    rightOpenBrackets += 1
                elif right[rightIdx] == "]":
                    rightOpenBrackets -= 1
                rightIdx += 1
            
            cmp = recursiveCompare(leftItem, rightItem)
            if cmp > 0:
                return 1
            elif cmp < 0:
                return -1
            leftIdx += 1
            rightIdx += 1
            leftItem = ""
            rightItem = ""
        
        # One of the lists ran out of elements
        if leftIdx == len(left) - 1:
            return 1
        elif rightIdx == len(right) - 1:
            return -1
        else:
            # We're trying to guess something here
            leftDiff = abs(leftIdx - len(left))
            rightDiff = abs(rightIdx - len(right))
            if leftDiff < rightDiff:
                return -1
            elif rightDiff < leftDiff:
                return 1
            else:
                return 0
            return 0
