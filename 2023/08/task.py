import re
import time
import math

def task1(input_lines: list[str]):
    directions = input_lines.pop(0)
    input_lines.pop(0)
    nodes = parse_graph(input_lines)
    print(nodes)
    path_len = walk_directions_get_length("AAA", "ZZZ", nodes, directions)
    print(path_len)


def task2(input_lines: list[str]):
    directions = input_lines.pop(0)
    input_lines.pop(0)
    nodes = parse_graph(input_lines)
    print(nodes)
    start_nodes = []
    for node in nodes.keys():
        if node.endswith("A"):
            start_nodes.append(node)
    print(start_nodes)
    all_lens: list[int] = []

    for start in start_nodes:
        all_lens.append(get_loop_length(start, nodes, directions))
    
    result = all_lens.pop(0)
    for path_len in all_lens:
        result *= path_len // math.gcd(path_len, result)

    print(result)


def parse_graph(nodes: list[str]) -> dict[str, (str, str)]:
    parsed_nodes = {}
    for node in nodes:
        m = re.compile(r"([\w]+) = \(([\w]+), ([\w]+)\)").match(node)
        parsed_nodes[m.group(1)] = (m.group(2), m.group(3))
    return parsed_nodes

def walk_directions_get_length(start: str, target: str, nodes: dict[str, (str, str)], directions: str) -> int:
    current = start
    current_direction_index = 0
    path_len = 0
    while current != target:
        if (directions[current_direction_index] == "R"):
            current = nodes[current][1]
        elif (directions[current_direction_index] == "L"):
            current = nodes[current][0]
        print(f"Walked {directions[current_direction_index]} to {current}")
        current_direction_index += 1
        if current_direction_index >= len(directions):
            current_direction_index = 0
        path_len += 1
    return path_len

def get_loop_length(start: str, nodes: dict[str, (str, str)], directions: str) -> int:
    current = start
    path_len = 0
    current_direction_index = 0

    while path_len == 0 or not current.endswith("Z"):
        path_len += 1
        if directions[current_direction_index] == "R":
            current = nodes[current][1]
        elif directions[current_direction_index] == "L":
            current = nodes[current][0]
        current_direction_index += 1
        current_direction_index %= len(directions)
    
    return path_len # Since the input data is very nice, the cycle from this first end to itself is the same length again, and no other ends are on the way