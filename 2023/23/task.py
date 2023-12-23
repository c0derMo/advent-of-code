import queue

def task1(input_lines: list[str]):
    path = find_longest_path(input_lines, (1, 0), (len(input_lines[0])-2, len(input_lines)-1))
    print(path)

def task2(input_lines: list[str]):
    compressed_graph, target_node = compress_graph(tuple(input_lines), (1, 0), (len(input_lines[0])-2, len(input_lines)-1))
    print(compressed_graph)
    path = bruteforce_on_graph(compressed_graph, 0, target_node)
    print(path)


def find_longest_path(grid: list[str], starting_position: (int, int), target: (int, int)):
    x_max = len(grid[0]) - 1
    y_max = len(grid) - 1

    # pos, len, visited tiles
    open_paths = [(starting_position, 0, [])]
    path_lengths = []

    while len(open_paths) > 0:
        position, path_length, visited_tiles = open_paths.pop(0)
        x, y = position

        if position == target:
            path_lengths.append(path_length)

        if x > 0 and grid[y][x-1] != "#" and grid[y][x] in [".", "<"] and (x-1, y) not in visited_tiles:
            open_paths.append(((x-1, y), path_length + 1, [position] + visited_tiles))
        if x < x_max and grid[y][x+1] != "#" and grid[y][x] in [".", ">"] and (x+1, y) not in visited_tiles:
            open_paths.append(((x+1, y), path_length + 1, [position] + visited_tiles))
        if y > 0 and grid[y-1][x] != "#" and grid[y][x] in [".", "^"] and (x, y-1) not in visited_tiles:
            open_paths.append(((x, y-1), path_length + 1, [position]+ visited_tiles))
        if y < y_max and grid[y+1][x] != "#" and grid[y][x] in [".", "v"] and (x, y+1) not in visited_tiles:
            open_paths.append(((x, y+1), path_length + 1, [position] + visited_tiles))
    
    return max(path_lengths)


def compress_graph(grid: tuple[str], starting_position: tuple[int, int], target: tuple[int, int]):
    x_max = len(grid[0]) - 1
    y_max = len(grid) - 1

    nodes = []
    edges = {}
    next_iteration = [starting_position]

    while len(next_iteration) != 0:
        next_next_iteration = set()

        for new_node in next_iteration:
            nodes.append(new_node)
            edges[new_node] = {}
            x, y = new_node

            if x > 0 and grid[y][x-1] != "#":
                next_pos, added_len = goto_next_cross_section(grid, (x-1, y), "l")
                edges[new_node][next_pos] = added_len
                if next_pos not in nodes:
                    next_next_iteration.add(next_pos)
            if x < x_max and grid[y][x+1] != "#":
                next_pos, added_len = goto_next_cross_section(grid, (x+1, y), "r")
                edges[new_node][next_pos] = added_len
                if next_pos not in nodes:
                    next_next_iteration.add(next_pos)
            if y > 0 and grid[y-1][x] != "#":
                next_pos, added_len = goto_next_cross_section(grid, (x, y-1), "u")
                edges[new_node][next_pos] = added_len
                if next_pos not in nodes:
                    next_next_iteration.add(next_pos)
            if y < y_max and grid[y+1][x] != "#":
                next_pos, added_len = goto_next_cross_section(grid, (x, y+1), "d")
                edges[new_node][next_pos] = added_len
                if next_pos not in nodes:
                    next_next_iteration.add(next_pos)
        next_iteration = [i for i in next_next_iteration]
    
    target_index = -1

    # Replacing coordinates with indices
    replaced_edges = {}
    for idx, coords in enumerate(nodes):
        replaced_edges[idx] = {}
        for edge, weight in edges[coords].items():
            target_idx = -1
            for t_id, t in enumerate(nodes):
                if t == edge:
                    target_idx = t_id
                    break
            if target_idx < 0:
                raise ValueError("Edge without target node :(")

            replaced_edges[idx][target_idx] = weight

        if coords == target:
            target_index = idx
    
    return replaced_edges, target_index

def bruteforce_on_graph(graph: dict[int, dict[int, int]], start_node: int, end_node: int):
    q = queue.SimpleQueue()
    q.put((start_node, 0, []))
    max_target_length = 0

    while not q.empty():
        current_node, path_length, previously_visited = q.get()

        if current_node == end_node:
            if path_length > max_target_length:
                max_target_length = path_length
            continue
            
        if end_node in graph[current_node]:
            if path_length + graph[current_node][end_node] > max_target_length:
                max_target_length = path_length + graph[current_node][end_node]
            continue
        
        new_prev_visited = previously_visited[:]
        new_prev_visited.append(current_node)
        for neighbor in graph[current_node].keys():
            if neighbor not in previously_visited:
                q.put((neighbor, path_length + graph[current_node][neighbor], new_prev_visited))

    return max_target_length
        

def goto_next_cross_section(grid: tuple[str], starting_position: tuple[int, int], direction: str) -> tuple[tuple[int, int], int]:
    x_max = len(grid[0]) - 1
    y_max = len(grid) - 1

    x, y = starting_position
    is_crossroads = False
    path_length = 1
    while not is_crossroads:
        possible_dirs = []
        next_dir = None
        next_pos = None

        if x > 0 and direction != "r" and grid[y][x-1] != "#":
            possible_dirs.append("l")
            next_dir = "l"
            next_pos = (x-1, y)
        if x < x_max and direction != "l" and grid[y][x+1] != "#":
            possible_dirs.append("r")
            next_dir = "r"
            next_pos = (x+1, y)
        if y > 0 and direction != "d" and grid[y-1][x] != "#":
            possible_dirs.append("u")
            next_dir = "u"
            next_pos = (x, y-1)
        if y < y_max and direction != "u" and grid[y+1][x] != "#":
            possible_dirs.append("d")
            next_dir = "d"
            next_pos = (x, y+1)
        
        if len(possible_dirs) != 1:
            is_crossroads = True
        else:
            x, y = next_pos
            direction = next_dir
            path_length += 1

    return ((x, y), path_length)