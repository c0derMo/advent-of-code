import re
import functools

def task1(input_lines: list[str]):
    total_sum = 0
    for idx, line in enumerate(input_lines):
        split_line = line.split(" ")
        input_line = split_line[0]
        batches = [int(x) for x in split_line[1].split(",")]

        possible_placements = possible_places(input_line, 0, batches, batches, input_line)
        print(f"Line {idx+1} has {possible_placements} possible placements")
        total_sum += possible_placements
    print(total_sum)

def task2(input_lines: list[str]):
    total_sum = 0
    for idx, line in enumerate(input_lines):
        split_line = line.split(" ")
        input_line = split_line[0]
        batches = [int(x) for x in split_line[1].split(",")]

        expanded_input = ((input_line + "?") * 5)[:-1]
        expanded_batches = batches * 5
        print(f"{expanded_input} {expanded_batches}")

        possible_placements = recursive_attempt(expanded_input, tuple(expanded_batches))
        print(f"Line {idx+1} has {possible_placements} possible placements")
        total_sum += possible_placements
    print(total_sum)


def pattern_to_regex(pattern: str) -> re.Pattern:
    regex = pattern.replace("?", r"[\.\?\#]")
    regex = regex.replace(".", r"\.")
    return re.compile(regex)

def possible_places(line: str, start_idx: int, batches_to_place: list[int], all_places: list[int], original_line: str) -> int:
    if len(batches_to_place) == 0:
        if is_correct_placement(line, all_places):
            # print(line)
            return 1
        else:
            # print(f"Cancelling {line} because placement is incorrect")
            return 0


    batch_to_place = "#" * batches_to_place[0]
    # print(f"Placing {batch_to_place} in {line} with {batches_to_place} remaining")
    result = 0
    for i in range(start_idx, len(line) - len(batch_to_place) + 1):
        new_line = line[:i] + batch_to_place + line[i + len(batch_to_place):]
        # print(new_line)

        if pattern_to_regex(original_line).match(new_line) == None:
            # print(f"Cancelling {new_line} because dots in original")
            continue

        result += possible_places(new_line, i + len(batch_to_place) + 1, batches_to_place[1:], all_places, original_line)
    return result

def is_correct_placement(line: str, batches: list[int]):
    placeholder = r"[\.\?]+"

    regex = r"^[\.\?]*"
    for batch in batches:
        regex += "#" * batch
        regex += placeholder
    regex = regex[:-1] + "*$"
    
    return re.compile(regex).match(line) != None



### Other, better attempt for calculation
@functools.cache
def recursive_attempt(pattern: str, batches: tuple[int, ...]) -> int:
    if len(batches) == 0:
        if "#" in pattern:
            return 0
        else:
            return 1
    
    if len(pattern) == 0:
        return 0

    next_character = pattern[0]
    
    result = 0
    if next_character == ".":
        result = handle_dot(pattern, batches)
    elif next_character == "#":
        result = handle_pound(pattern, batches)
    elif next_character == "?":
        dr = handle_dot(pattern, batches)
        pr = handle_pound(pattern, batches)
        # print(f".{pattern[1:]} ({batches}) -> {dr}")
        # print(f"#{pattern[1:]} ({batches}) -> {pr}")
        result = dr + pr
    # print(f"{pattern} ({batches}) -> {result}")
    return result

    
def handle_dot(pattern: str, batches: tuple[int, ...]) -> int:
    return recursive_attempt(pattern[1:], batches)

def handle_pound(pattern: str, batches: tuple[int, ...]) -> int:
    next_batch = batches[0]
    if len(pattern) < next_batch:
        return 0
    
    for i in range(next_batch):
        if pattern[i] != "#" and pattern[i] != "?":
            return 0
    
    if len(pattern) > next_batch:
        if pattern[next_batch] == "#":
            return 0
        else:
            return recursive_attempt(pattern[next_batch + 1:], batches[1:])
    else:
        return recursive_attempt(pattern[next_batch:], batches[1:])