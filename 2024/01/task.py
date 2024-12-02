def task1(input_lines: list[str]):
    left = []
    right = []

    for line in input_lines:
        nums = line.split()
        left.append(int(nums[0]))
        right.append(int(nums[1]))
    
    left.sort()
    right.sort()

    distance_total = 0

    for _ in range(len(left)):
        a = left.pop()
        b = right.pop()
        diff = abs(a - b)

        distance_total += diff

    print(distance_total)

def task2(input_lines: list[str]):
    left = []
    right = {}

    for line in input_lines:
        nums = line.split()
        left.append(int(nums[0]))
        r_num = int(nums[1])
        if r_num in right:
            right[r_num] = right[r_num] + 1
        else:
            right[r_num] = 1
    
    similarity = 0
    for x in left:
        if x in right:
            similarity += x * right[x]
    
    print(similarity)