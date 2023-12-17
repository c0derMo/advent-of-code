import heapq

def task1(input_lines: list[str]):
    grid = lines_to_grid(input_lines)
    leak = attempt_with_djikstra(grid, (0, 0), (len(grid)-1, len(grid[0])-1))
    print(leak)

def task2(input_lines: list[str]):
    grid = lines_to_grid(input_lines)
    leak = attempt_with_djikstra(grid, (0, 0), (len(grid)-1, len(grid[0])-1), 4, 10)
    print(leak)


def lines_to_grid(lines: list[str]) -> list[list[int]]:
    grid = []
    for x in range(len(lines[0])):
        col = []
        for y in range(len(lines)):
            col.append(int(lines[y][x]))
        grid.append(col)
    return grid

def attempt_with_djikstra(grid: list[list[int]], start: tuple[int, int], end: tuple[int, int], min_move=1, max_move=3) -> tuple[int, str]:
    distances = []
    for _ in range(len(grid)):
        col = []
        for _ in range(len(grid[0])):
            col.append([-1, -1])
        distances.append(col)
    
    x_max = len(grid) - 1
    y_max = len(grid[0]) - 1

    pq = []
    heapq.heappush(pq, (0, start, ""))

    while len(pq) > 0:
        leak_from_start, position, direction = heapq.heappop(pq)
        if position == end:
            return leak_from_start, direction
        x, y = position
        if len(direction) > 0:
            distances_index = 0 if direction[-1] == "u" or direction[-1] == "d" else 1
            if distances[x][y][distances_index] != -1:
                continue

            distances[x][y][distances_index] = leak_from_start
        else:
            distances[x][y] = [leak_from_start, leak_from_start]

        if direction == "" or direction.endswith("d") or direction.endswith("u"):
            leak_l = 0
            leak_r = 0
            for i in range(1, max_move+1):
                if x - i >= 0:
                    leak_l += grid[x-i][y]
                    if i >= min_move:
                        heapq.heappush(pq, (leak_from_start + leak_l, (x-i, y), direction + "l"*i))    
                if x + i <= x_max:
                    leak_r += grid[x+i][y]
                    if i >= min_move:
                        heapq.heappush(pq, (leak_from_start + leak_r, (x+i, y), direction + "r"*i))
        if direction == "" or direction.endswith("r") or direction.endswith("l"):
            leak_u = 0
            leak_d = 0
            for i in range(1, max_move+1):
                if y - i >= 0:
                    leak_u += grid[x][y-i]
                    if i >= min_move:
                        heapq.heappush(pq, (leak_from_start + leak_u, (x, y-i), direction + "u"*i))
                if y + i <= y_max:
                    leak_d += grid[x][y+i]
                    if i >= min_move:
                        heapq.heappush(pq, (leak_from_start + leak_d, (x, y+i), direction + "d"*i))
    raise KeyError("Didnt find path to end :(")