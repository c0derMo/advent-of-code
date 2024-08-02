import re

def task1(input_lines: list[str]):
    print("Building map")
    connections = build_map(input_lines)
    # print(connections)
    print("Building possible paths")

    paths: list[tuple[int, list[str]]] = []
    for starting_location in connections.keys():
        paths.extend(build_all_paths_recursively(connections, starting_location, 0))
    
    # for path in paths:
        # print(f"{' -> '.join(path[1])} = {path[0]}")

    paths.sort(key=lambda x: x[0])
    print(paths[0][0])

def task2(input_lines: list[str]):
    connections = build_map(input_lines)

    paths: list[tuple[int, list[str]]] = []
    for starting_location in connections.keys():
        paths.extend(build_all_paths_recursively(connections, starting_location, 0))

    paths.sort(key=lambda x: x[0])
    print(paths[-1][0])


def build_all_paths_recursively(connections: dict[str, dict[str, int]], current_position: str, current_length: int, previous_path: list[str] = []) -> list[tuple[int, list[str]]]:
    all_locations = connections.keys()
    new_path = [x for x in previous_path]
    new_path.append(current_position)
    if len(new_path) == len(all_locations):
        return [(current_length, new_path)]
    
    future_paths = []
    for possible_dest in connections[current_position].keys():
        if possible_dest in previous_path:
            continue

        future_paths.extend(build_all_paths_recursively(connections, possible_dest, current_length + connections[current_position][possible_dest], new_path))
    
    return future_paths


def build_map(lines: list[str]) -> dict[str, dict[str, int]]:
    result = {}
    pattern = re.compile("^(\\w+) to (\\w+) = (\\d+)$")

    for line in lines:
        matcher = pattern.match(line)
        if not matcher:
            raise ValueError(f"Line {line} does not match regex")

        src = matcher.group(1)
        dest = matcher.group(2)
        dist = int(matcher.group(3))

        if src not in result:
            result[src] = {}
        if dest not in result:
            result[dest] = {}
        result[src][dest] = dist
        result[dest][src] = dist
    
    return result