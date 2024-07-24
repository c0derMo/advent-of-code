import hashlib

def task1(input_lines: list[str]):
    num = 1
    key = input_lines[0]
    while True:
        h = try_hash(key, num)
        if has_leading_zeroes(h):
            print(num)
            return
        else:
            num += 1
        
        if num % 10000 == 0:
            print(f"Failed num {num}")

def task2(input_lines: list[str]):
    num = 117946
    key = input_lines[0]
    while True:
        h = try_hash(key, num)
        if has_leading_zeroes(h, 6):
            print(num)
            return
        else:
            num += 1
        
        if num % 10000 == 0:
            print(f"Failed num {num}")

def try_hash(key: str, to_hash: int) -> str:
    h = hashlib.md5((key + str(to_hash)).encode())
    return h.hexdigest()

def has_leading_zeroes(check: str, amount: int = 5) -> bool:
    return check.startswith("0" * amount)