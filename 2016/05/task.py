import hashlib

def task1(input_lines: list[str]):
    start_idx = 0
    pw = ""
    door_id = input_lines[0]
    for _ in range(8):
        char, next_idx = get_hash_starting_with_5_zeros(door_id, start_idx)
        pw += char[5]
        start_idx = next_idx + 1
        print(pw)

def task2(input_lines: list[str]):
    start_idx = 0
    pw = ["_","_","_","_","_","_","_","_"]
    door_id = input_lines[0]
    while "_" in pw:
        h = hashlib.md5((door_id + str(start_idx)).encode()).hexdigest()
        if h.startswith("00000") and h[5] in "01234567" and pw[int(h[5])] == "_":
            pw[int(h[5])] = h[6]
            print("".join(pw))
        start_idx += 1

def get_hash_starting_with_5_zeros(door_id: str, starting_index: int) -> tuple[str, int]:
    idx = starting_index
    while True:
        to_hash = door_id + str(idx)
        h = hashlib.md5(to_hash.encode(), usedforsecurity=False)
        if h.hexdigest().startswith("00000"):
            return h.hexdigest(), idx
        idx += 1