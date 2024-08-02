from abc import ABC, abstractmethod
from dataclasses import dataclass
import re

def task1(input_lines: list[str]):
    # operations = [parse_line(x) for x in input_lines]
    # for op in operations:
    #     print(op)
    # result_op = build_tree_with_cache(operations, "a")
    # print(result_op.execute())

    # Replacement Strategy
    operations = input_lines
    replacement = "x"
    value = 0
    while replacement != None and len(operations) > 0:
        operations, replacement, value = replacement_strategy(operations)
        print(f"Replaced {replacement} with {value}. Remaining ops: {len(operations)}")
        if replacement == "a":
            break
    print(operations)
    print(replacement)
    print(value)

def task2(input_lines: list[str]):
    # Replacement Strategy
    operations = input_lines
    replacement = "x"
    value = 0
    while replacement != None and len(operations) > 0:
        operations, replacement, value = replacement_strategy(operations)
        print(f"Replaced {replacement} with {value}. Remaining ops: {len(operations)}")
        if replacement == "a":
            break
    
    if replacement != "a":
        raise ValueError(f"We didnt end with a the first time NotLikeThis")
    
    new_ops = []
    for op in input_lines:
        if op.endswith(" -> b"):
            new_ops.append(f"{value} -> b")
        else:
            new_ops.append(op)
    replacement = "x"
    value = 0
    while replacement != None and len(new_ops) > 0:
        new_ops, replacement, value = replacement_strategy(new_ops)
        print(f"Replaced {replacement} with {value}. Remaining ops: {len(new_ops)}")
        if replacement == "a":
            break
    print(operations)
    print(replacement)
    print(value)

def replacement_strategy(operations: list[str]) -> tuple[list[str], str, int]:
    for line in operations:
        left_single_number = re.match(r"^(\d+) -> ([a-z]+)$", line)
        if left_single_number:
            return replace(operations, left_single_number.group(2), int(left_single_number.group(1)), line)
        not_number = re.match(r"^NOT (\d+) -> ([a-z]+)$", line)
        if not_number:
            result = ~ int(not_number.group(1))
            if result < 0:
                result = (result % 65535) + 1
            if result > 65535:
                result = result % 65535
            var = not_number.group(2)
            return replace(operations, var, result, line)
        two_side_op = re.match(r"^(\d+) ([A-Z]+) (\d+) -> ([a-z]+)$", line)
        if two_side_op:
            lh = int(two_side_op.group(1))
            op = two_side_op.group(2)
            rh = int(two_side_op.group(3))
            var = two_side_op.group(4)
            if op == "AND":
                result = lh & rh
            elif op == "OR":
                result = lh | rh
            elif op == "LSHIFT":
                result = lh << rh
            elif op == "RSHIFT":
                result = lh >> rh
            else:
                raise ValueError(f"Unknown op {op} in {line}")
            return replace(operations, var, result, line)
    return operations, None, None

def replace(operations: list[str], result: str, val: int, line_to_remove: str) -> tuple[list[str], str, int]:
    result_lines = []
    for line in operations:
        if line == line_to_remove:
            continue

        both_matcher = re.match(f"^{result} ([A-Z]+) {result} -> ([a-z]+)$", line)
        lhd_matcher = re.match(f"^{result} ([A-Z]+ [a-z0-9]+ -> [a-z]+)$", line)
        rhd_matcher = re.match(f"^([a-z0-9]+ [A-Z]+) {result} -> ([a-z]+)$", line)
        single_val = re.match(f"^{result} -> ([a-z]+)$", line)
        not_matcher = re.match(f"^NOT {result} -> ([a-z]+)$", line)
        if both_matcher:
            result_lines.append(f"{val} {both_matcher.group(1)} {val} -> {both_matcher.group(2)}")
            # print(f"{line} became {result_lines[-1]}")
        elif lhd_matcher:
            result_lines.append(f"{val} {lhd_matcher.group(1)}")
            # print(f"{line} became {result_lines[-1]}")
        elif rhd_matcher:
            result_lines.append(f"{rhd_matcher.group(1)} {val} -> {rhd_matcher.group(2)}")
            # print(f"{line} became {result_lines[-1]}")
        elif single_val:
            result_lines.append(f"{val} -> {single_val.group(1)}")
            # print(f"{line} became {result_lines[-1]}")
        elif not_matcher:
            result_lines.append(f"NOT {val} -> {not_matcher.group(1)}")
            # print(f"{line} became {result_lines[-1]}")
        else:
            result_lines.append(line)
    return (result_lines, result, val)