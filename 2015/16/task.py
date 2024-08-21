from dataclasses import dataclass
import re
from typing import Optional


def task1(input_lines: list[str]):
    correct_sue = Sue(-1, 3, 7, 2, 3, 0, 0, 5, 3, 2, 1)

    sues = [parse_sue(x) for x in input_lines]

    valid_sues = [x for x in sues if inaccurate_sue_matcher(x, correct_sue)]

    print(len(valid_sues))
    print(valid_sues[0].num)

def task2(input_lines: list[str]):
    correct_sue = Sue(-1, 3, 7, 2, 3, 0, 0, 5, 3, 2, 1)

    sues = [parse_sue(x) for x in input_lines]

    valid_sues = [x for x in sues if inaccurate_sue_matcher_v2(x, correct_sue)]

    print(len(valid_sues))
    print(valid_sues[0].num)


@dataclass
class Sue:
    num: int
    children: Optional[int] = None
    cats: Optional[int] = None
    samoyeds: Optional[int] = None
    pomeranians: Optional[int] = None
    akitas: Optional[int] = None
    vizslas: Optional[int] = None
    goldfish: Optional[int] = None
    trees: Optional[int] = None
    cars: Optional[int] = None
    perfumes: Optional[int] = None


def parse_sue(sue: str) -> Sue:
    pattern = re.compile(r"Sue (\d+): (.+)")
    matcher = pattern.match(sue)
    if matcher is None:
        raise ValueError(f"Sue {sue} does not match regex")
    sue_num = int(matcher.group(1))
    sue_intel = matcher.group(2).split(", ")
    result_sue = Sue(sue_num)
    
    intel_pattern = re.compile(r"(\w+): (\d+)")
    for intel in sue_intel:
        intel_matcher = intel_pattern.match(intel)
        if intel_matcher is None:
            raise ValueError(f"Intel {intel} does not match regex ${sue_num}")
        intel_val = int(intel_matcher.group(2))
        if intel_matcher.group(1) == "children":
            result_sue.children = intel_val
        elif intel_matcher.group(1) == "cats":
            result_sue.cats = intel_val
        elif intel_matcher.group(1) == "samoyeds":
            result_sue.samoyeds = intel_val
        elif intel_matcher.group(1) == "pomeranians":
            result_sue.pomeranians = intel_val
        elif intel_matcher.group(1) == "akitas":
            result_sue.akitas = intel_val
        elif intel_matcher.group(1) == "vizslas":
            result_sue.vizslas = intel_val
        elif intel_matcher.group(1) == "goldfish":
            result_sue.goldfish = intel_val
        elif intel_matcher.group(1) == "trees":
            result_sue.trees = intel_val
        elif intel_matcher.group(1) == "cars":
            result_sue.cars = intel_val
        elif intel_matcher.group(1) == "perfumes":
            result_sue.perfumes = intel_val
    return result_sue

def inaccurate_sue_matcher(inaccurate: Sue, accurate: Sue) -> bool:
    if inaccurate.children != None and inaccurate.children != accurate.children:
        return False
    if inaccurate.cats != None and inaccurate.cats != accurate.cats:
        return False
    if inaccurate.samoyeds != None and inaccurate.samoyeds != accurate.samoyeds:
        return False
    if inaccurate.pomeranians != None and inaccurate.pomeranians != accurate.pomeranians:
        return False
    if inaccurate.akitas != None and inaccurate.akitas != accurate.akitas:
        return False
    if inaccurate.vizslas != None and inaccurate.vizslas != accurate.vizslas:
        return False
    if inaccurate.goldfish != None and inaccurate.goldfish != accurate.goldfish:
        return False
    if inaccurate.trees != None and inaccurate.trees != accurate.trees:
        return False
    if inaccurate.cars != None and inaccurate.cars != accurate.cars:
        return False
    if inaccurate.perfumes != None and inaccurate.perfumes != accurate.perfumes:
        return False
    return True

def inaccurate_sue_matcher_v2(inaccurate: Sue, accurate: Sue) -> bool:
    if inaccurate.children != None and inaccurate.children != accurate.children:
        return False
    if inaccurate.cats != None and inaccurate.cats <= accurate.cats:
        return False
    if inaccurate.samoyeds != None and inaccurate.samoyeds != accurate.samoyeds:
        return False
    if inaccurate.pomeranians != None and inaccurate.pomeranians >= accurate.pomeranians:
        return False
    if inaccurate.akitas != None and inaccurate.akitas != accurate.akitas:
        return False
    if inaccurate.vizslas != None and inaccurate.vizslas != accurate.vizslas:
        return False
    if inaccurate.goldfish != None and inaccurate.goldfish >= accurate.goldfish:
        return False
    if inaccurate.trees != None and inaccurate.trees <= accurate.trees:
        return False
    if inaccurate.cars != None and inaccurate.cars != accurate.cars:
        return False
    if inaccurate.perfumes != None and inaccurate.perfumes != accurate.perfumes:
        return False
    return True