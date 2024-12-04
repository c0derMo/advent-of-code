import re

def task1(input_lines: list[str]):
    decomp_len = 0
    idx = 0
    ip = input_lines[0]
    while idx < len(ip):
        if ip[idx] != "(":
            decomp_len += 1
            idx += 1
        else:
            pattern = re.compile(r"\((\d+)x(\d+)\)")
            matcher = pattern.match(ip[idx:])
            if matcher is None:
                raise ValueError("error while regexing")
            wanted_len = int(matcher.group(1))
            wanted_repeats = int(matcher.group(2))
            idx += len(matcher.group(0))
            actual_len = min(len(ip[idx:]), wanted_len)
            decomp_len += actual_len * wanted_repeats
            idx += actual_len
    print(decomp_len)

def task2(input_lines: list[str]):
    decomp_len = 0
    idx = 0
    ip = input_lines[0]
    while idx < len(ip):
        if ip[idx] != "(":
            decomp_len += 1
            idx += 1
        else:
            pattern = re.compile(r"\((\d+)x(\d+)\)")
            matcher = pattern.match(ip[idx:])
            if matcher is None:
                raise ValueError("error while regexing")
            wanted_len = int(matcher.group(1))
            wanted_repeats = int(matcher.group(2))

            idx += len(matcher.group(0))
            dc = get_decomped_length(wanted_repeats, wanted_len, ip[idx:])
            idx += dc[1]
            decomp_len += dc[0]
    print(decomp_len)


def get_decomped_length(repeats: int, repeating_chars: int, remainder_string: str) -> tuple[int, int]:
    # print(f"Calculating for {repeating_chars}x{repeats}: got string {remainder_string}")
    pattern = re.compile(r"\((\d+)x(\d+)\)")
    decomp_len = 0
    check_idx = 0
    # print(f"Checking for patterns inside {remainder_string[:repeating_chars]}")
    while check_idx < repeating_chars:
        match = pattern.match(remainder_string[check_idx:])
        if match is None:
            decomp_len += repeats
            check_idx += 1
            continue
        new_repeats = int(match.group(2))
        new_chars = int(match.group(1))
        new_remainder = remainder_string[(len(match.group(0)) + check_idx):]

        new_dc_len = get_decomped_length(new_repeats, new_chars, new_remainder)
        check_idx += len(match.group(0))
        check_idx += new_dc_len[1]
        decomp_len += repeats * new_dc_len[0]
    # print(f"len for {repeating_chars}x{repeats}: {decomp_len} ({check_idx})")
    return (decomp_len, check_idx)