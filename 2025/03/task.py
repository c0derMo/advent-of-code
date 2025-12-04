def task1(input_lines: list[str]):
    res = 0
    for line in input_lines:
        batteries = [int(x) for x in line]
        biggest = max(batteries)
        biggest_index = batteries.index(biggest)
        if biggest_index == len(batteries)-1:
            biggest_following = max(batteries[:-1])
            biggest_following, biggest = biggest, biggest_following
        else:
            biggest_following = max(batteries[biggest_index+1:])
        num = biggest * 10 + biggest_following
        print(num)
        res += num
    print(res)

def task2(input_lines: list[str]):
    res = 0

    for line in input_lines:
        batteries = [int(x) for x in line]
        toggles = [False for _ in line]
        while toggles.count(True) != 12:
            toggles = toggle_nth_biggest(batteries, toggles)
        num = build_number(batteries, toggles)
        print(num)
        res += num
    
    print(res)

def toggle_nth_biggest(nums: list[int], toggles: list[bool]) -> list[bool]:
    possible_new_toggles: list[list[bool]] = []

    for i in range(len(toggles)):
        if toggles[i]:
            continue
        new_toggles = list(toggles)
        new_toggles[i] = True
        possible_new_toggles.append(new_toggles)

    # Finding the largest
    largest_idx = 0
    for i in range(1, len(possible_new_toggles)):
        if build_number(nums, possible_new_toggles[i]) > build_number(nums, possible_new_toggles[largest_idx]):
            largest_idx = i

    return possible_new_toggles[largest_idx]

def build_number(nums: list[int], toggles: list[bool]) -> int:
    res = ""
    for idx in range(len(nums)):
        if toggles[idx]:
            res += str(nums[idx])
    return int(res)