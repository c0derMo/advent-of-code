import re

def task1(input_lines: list[str]):
    registers = {
        "a": 0,
        "b": 0
    }
    pc = 0

    while pc >= 0 and pc < len(input_lines):
        instruction_info = parse_instruction(input_lines[pc])
        if instruction_info[0] == "hlf":
            registers[instruction_info[1]] /= 2
            pc += 1
        elif instruction_info[0] == "tpl":
            registers[instruction_info[1]] *= 3
            pc += 1
        elif instruction_info[0] == "inc":
            registers[instruction_info[1]] += 1
            pc += 1
        elif instruction_info[0] == "jmp":
            pc += instruction_info[1]
        elif instruction_info[0] == "jie":
            if registers[instruction_info[1]] % 2 == 0:
                pc += instruction_info[2]
            else:
                pc += 1
        elif instruction_info[0] == "jio":
            if registers[instruction_info[1]] == 1:
                pc += instruction_info[2]
            else:
                pc += 1

    print(registers["b"])

def task2(input_lines: list[str]):
    registers = {
        "a": 1,
        "b": 0
    }
    pc = 0

    while pc >= 0 and pc < len(input_lines):
        instruction_info = parse_instruction(input_lines[pc])
        if instruction_info[0] == "hlf":
            registers[instruction_info[1]] /= 2
            pc += 1
        elif instruction_info[0] == "tpl":
            registers[instruction_info[1]] *= 3
            pc += 1
        elif instruction_info[0] == "inc":
            registers[instruction_info[1]] += 1
            pc += 1
        elif instruction_info[0] == "jmp":
            pc += instruction_info[1]
        elif instruction_info[0] == "jie":
            if registers[instruction_info[1]] % 2 == 0:
                pc += instruction_info[2]
            else:
                pc += 1
        elif instruction_info[0] == "jio":
            if registers[instruction_info[1]] == 1:
                pc += instruction_info[2]
            else:
                pc += 1

    print(registers["b"])

half_regex = re.compile(r"hlf ([ab])")
triple_regex = re.compile(r"tpl ([ab])")
increment_regex = re.compile(r"inc ([ab])")
jump_regex = re.compile(r"jmp ([+-]\d+)")
jump_if_even_regex = re.compile(r"jie ([ab]), ([+-]\d+)")
jump_if_one_regex = re.compile(r"jio ([ab]), ([+-]\d+)")

def parse_instruction(instruction: str) -> tuple[str, str, str]:
    half_matcher = half_regex.match(instruction)
    if half_matcher is not None:
        return "hlf", half_matcher.group(1), None
    triple_matcher = triple_regex.match(instruction)
    if triple_matcher is not None:
        return "tpl", triple_matcher.group(1), None
    increment_matcher = increment_regex.match(instruction)
    if increment_matcher is not None:
        return "inc", increment_matcher.group(1), None
    jump_matcher = jump_regex.match(instruction)
    if jump_matcher is not None:
        return "jmp", int(jump_matcher.group(1))
    jump_if_even_matcher = jump_if_even_regex.match(instruction)
    if jump_if_even_matcher is not None:
        return "jie", jump_if_even_matcher.group(1), int(jump_if_even_matcher.group(2))
    jump_if_one_matcher = jump_if_one_regex.match(instruction)
    if jump_if_one_matcher is not None:
        return "jio", jump_if_one_matcher.group(1), int(jump_if_one_matcher.group(2))
    raise ValueError(f"Unparsable instruction: {instruction}")