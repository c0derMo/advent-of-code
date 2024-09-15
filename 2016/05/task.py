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
        h, next_idx = get_hash_starting_with_5_zeros(door_id, start_idx)
        if h[5] not in ["0", "1", "2", "3", "4", "5", "6", "7"]:
            continue
        pos = int(h[5])
        if pw[pos] != "_":
            continue
        pw[pos] = h[6]
        start_idx = next_idx + 1
        print("".join(pw))

def get_hash_starting_with_5_zeros(door_id: str, starting_index: int) -> tuple[str, int]:
    idx = starting_index
    while True:
        to_hash = door_id + str(idx)
        h = hashlib.md5(to_hash.encode(), usedforsecurity=False)
        if h.hexdigest().startswith("00000"):
            return h.hexdigest(), idx
        idx += 1