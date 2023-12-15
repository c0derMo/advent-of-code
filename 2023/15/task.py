import functools

def task1(input_lines: list[str]):
    result = 0
    for to_hash in input_lines[0].split(","):
        result += hash_string_recursively(to_hash)
    print(result)

def task2(input_lines: list[str]):
    boxes: list[list[tuple[str, int]]] = []
    for _ in range(256):
        boxes.append([])
    
    for to_hash in input_lines[0].split(","):
        if to_hash.endswith("-"):
            box = hash_string_recursively(to_hash[:-1])
            for lens in boxes[box]:
                if lens[0] == to_hash[:-1]:
                    boxes[box].remove(lens)
        elif "=" in to_hash:
            label = to_hash.split("=")[0]
            strength = int(to_hash.split("=")[1])
            box = hash_string_recursively(label)
            replaced = False
            for l_id, lens in enumerate(boxes[box]):
                if lens[0] == label:
                    boxes[box][l_id] = (label, strength)
                    replaced = True
                    break
            if not replaced:
                boxes[box].append((label, strength))
        else:
            raise ValueError(f"{to_hash} contains no operator")
    
    focussing_power = calculate_focussing_power(boxes)
    print(focussing_power)


@functools.cache
def hash_string_recursively(to_hash: str, init=0) -> int:
    if len(to_hash) == 0:
        return init
    
    result = init
    current_char = to_hash[0]
    result += ord(current_char)
    result *= 17
    result %= 256
    return hash_string_recursively(to_hash[1:], result)

def calculate_focussing_power(boxes: list[list[tuple[str, int]]]) -> int:
    result = 0
    for b_id, box in enumerate(boxes):
        for l_id, lens in enumerate(box):
            print(f"{lens[0]}: Box {b_id+1} * Slot {l_id+1} * Strength {lens[1]}")
            result += (b_id+1) * (l_id+1) * lens[1]
    return result