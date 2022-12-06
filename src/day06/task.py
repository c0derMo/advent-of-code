def task1(inputLines):
    line = inputLines[0]
    for i in range(4, len(line)):
        if checkPreviousDistinct(line, i, 4):
            print("Check previous distinct result:")
            print(i)
            break
        # if line[i:i+1] != line[i-1:i] and line[i:i+1] != line[i-2:i-1]and line[i:i+1] != line[i-3:i-2] \
        #     and line[i-1:i] != line[i-2:i-1] and line[i-1:i] != line[i-3:i-2] \
        #         and line[i-2:i-1] != line[i-3:i-2]:
        #     print(line[i:i+1])
        #     print(line[i-1:i])
        #     print(line[i-2:i-1])
        #     print(line[i-3:i-2])
        #     print(i+1)
        #     break

def task2(inputLines):
    line = inputLines[0]
    for i in range(4, len(line)):
        if checkPreviousDistinct(line, i, 14):
            print(i)
            break


def checkPreviousDistinct(word, startingIndex, numChecks):
    chars = []
    chars.append(word[startingIndex-1:startingIndex])
    i = 1
    while i < numChecks:
        if word[startingIndex-i-1:startingIndex-i] in chars:
            return False
        else:
            chars.append(word[startingIndex-i-1:startingIndex-i])
        i += 1
    return True