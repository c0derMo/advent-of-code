import re

mul_re = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
total_re = re.compile(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)")

def task1(input_lines: list[str]):
    total = 0
    for line in input_lines:
        mults = re.findall(mul_re, line)
        for mult in mults:
            total += int(mult[0]) * int(mult[1])
    print(total)

def task2(input_lines: list[str]):
    total = 0
    enabled = True
    for line in input_lines:
        instructions = re.findall(total_re, line)
        for instruction in instructions:
            if instruction == "do()":
                enabled = True
            elif instruction == "don't()":
                enabled = False
            elif enabled:
                mult = re.match(mul_re, instruction)
                total += int(mult.group(1)) * int(mult.group(2))
    print(total)