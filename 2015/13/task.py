import re
import itertools

def task1(input_lines: list[str]):
    happiness_map = build_happiness_map(input_lines)
    people = happiness_map.keys()
    seating_options = list(itertools.permutations(people))
    
    max_happiness = 0
    for option in seating_options:
        happiness = get_happiness(happiness_map, option)
        if happiness > max_happiness:
            max_happiness = happiness
    print(max_happiness)

def task2(input_lines: list[str]):
    happiness_map = build_happiness_map(input_lines)

    happiness_map["self"] = {}
    for person in happiness_map.keys():
        happiness_map["self"][person] = 0
        happiness_map[person]["self"] = 0

    people = happiness_map.keys()
    seating_options = list(itertools.permutations(people))
    
    max_happiness = 0
    for option in seating_options:
        happiness = get_happiness(happiness_map, option)
        if happiness > max_happiness:
            max_happiness = happiness
    print(max_happiness)


def get_happiness(happiness_map: dict[str, dict[str, int]], seating: list[str]) -> int:
    total_happiness = 0

    for i in range(len(seating)):
        sitting_here = seating[i]
        l_neighbor = seating[i-1]
        r_neighbor = seating[(i+1) % len(seating)]

        total_happiness += happiness_map[sitting_here][l_neighbor]
        total_happiness += happiness_map[sitting_here][r_neighbor]
    return total_happiness


def build_happiness_map(lines: list[str]) -> dict[str, dict[str, int]]:
    result = {}
    pattern = re.compile("^(\\w+) would (gain|lose) (\\d+) happiness units by sitting next to (\\w+).$")

    for line in lines:
        m = pattern.match(line)
        if not m:
            raise ValueError(f"{line} does not match regex")

        src = m.group(1)
        dest = m.group(4)
        happiness = int(m.group(3))
        if m.group(2) == "lose":
            happiness = -happiness
        
        if src not in result:
            result[src] = {}
        if dest not in result:
            result[dest] = {}
        
        result[src][dest] = happiness
    return result