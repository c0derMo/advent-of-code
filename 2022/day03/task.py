def task1(inputLines):
    score = 0
    for line in inputLines:
        leftHalf = line[:int(len(line)/2)]
        rightHalf = line[int(len(line)/2):]
        # print(leftHalf)
        # print(rightHalf)
        for char in leftHalf:
            if char in rightHalf:
                # print(char)
                if char.isupper():
                    score += ord(char)-38
                    # print(ord(char)-38)
                else:
                    score += ord(char)-96
                    # print(ord(char)-64)
                break

    print(score)

def task2(inputLines):
    score = 0
    for group in range(0, int(len(inputLines)/3)):
        elfOne = inputLines[(group*3)]
        elfTwo = inputLines[(group*3)+1]
        elfThree = inputLines[(group*3)+2]
        for char in elfOne:
            if char in elfTwo and char in elfThree:
                if char.isupper():
                    score += ord(char)-38
                else:
                    score += ord(char)-96
                break
    print(score)
