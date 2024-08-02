import re

def task1(input_lines: list[str]):
    total_sum = 0
    for line in input_lines:
        # print(line)
        # print(len(line))
        # print(length_of_contained_string(line))
        total_sum += len(line) - length_of_contained_string(line)
    print(total_sum)

def task2(input_lines: list[str]):
    total_sum = 0
    for line in input_lines:
        # print(line)
        # print(len(line))
        # print(length_of_escaped_string(line))
        total_sum += length_of_escaped_string(line) - len(line)
    print(total_sum)


def length_of_contained_string(input_string: str) -> int:
    translated = re.sub(r'(\\\\)|(\\")|(\\x[0-9A-Fa-f]{2})', "x", input_string)
    translated = translated.replace('"', "")
    return len(translated)

def length_of_escaped_string(input_string: str) -> int:
    translated = input_string.replace('\\', '\\\\')
    translated = translated.replace('"', '\\"')
    translated = '"' + translated + '"'
    # print(translated)
    return len(translated)