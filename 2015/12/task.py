import re
import json
from typing import Any

def task1(input_lines: list[str]):
    data = json.loads(input_lines[0])
    all_numbers = find_all_numbers(data)
    print(sum(all_numbers))

def task2(input_lines: list[str]):
    data = json.loads(input_lines[0])
    all_numbers = find_all_numbers_ignoring_red(data)
    print(sum(all_numbers))


def find_all_numbers(to_scan: Any) -> list[int]:
    numbers = []

    if type(to_scan) is str:
        return []
    
    if type(to_scan) is int:
        return [int(to_scan)]

    if type(to_scan) is list:
        for item in to_scan:
            numbers.extend(find_all_numbers(item))
    
    if type(to_scan) is dict:
        for key in to_scan.keys():
            numbers.extend(find_all_numbers(key))
            numbers.extend(find_all_numbers(to_scan[key]))

    return numbers

def find_all_numbers_ignoring_red(to_scan: Any) -> list[int]:
    numbers = []

    if type(to_scan) is str:
        return []
    
    if type(to_scan) is int:
        return [int(to_scan)]

    if type(to_scan) is dict:
        if "red" in to_scan.values():
            return []
        for key in to_scan.keys():
            numbers.extend(find_all_numbers_ignoring_red(key))
            numbers.extend(find_all_numbers_ignoring_red(to_scan[key]))

    if type(to_scan) is list:
        for item in to_scan:
            numbers.extend(find_all_numbers_ignoring_red(item))

    return numbers