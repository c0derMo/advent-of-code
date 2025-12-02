def task1(input_lines: list[str]):
    ranges = input_lines[0].split(",")
    valid_invalids: list[int] = []
    for r in ranges:
        start, end = [int(x) for x in r.split("-")]

        invalids = generate_invalid(end)
        for invalid in invalids:
            if invalid >= start and invalid <= end:
                # print(f"Found invalid {invalid}")
                valid_invalids.append(invalid)
    print(sum(valid_invalids))

def task2(input_lines: list[str]):
    ranges = input_lines[0].split(",")
    valid_invalids: list[int] = []
    for r in ranges:
        start, end = [int(x) for x in r.split("-")]

        invalids = generate_invalid_v2(end)
        for invalid in invalids:
            if invalid >= start and invalid <= end:
                # print(f"Found invalid {invalid}")
                valid_invalids.append(invalid)
    print(sum(valid_invalids))


def generate_invalid(end: int) -> list[int]:
    result: list[int] = []
    i = 1
    while int(str(i) + str(i)) <= end:
        result.append((int(str(i) + str(i))))
        i += 1
    return result

def generate_invalid_v2(end: int) -> set[int]:
    result: set[int] = set()
    i = 1
    while int(str(i) + str(i)) <= end:
        repeats = 2
        while int(repeats * str(i)) <= end:
            result.add(int(repeats * str(i)))
            repeats += 1
        i += 1
    return result