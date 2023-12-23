from typing import Any

def task1(input_lines: list[str]):
    x_max, y_max, z_max, blocks = parse_blocks(input_lines)
    supported_by = drop_and_find_supporters(x_max, y_max, z_max, blocks)
    amount_desintegratable = find_desintegratable_bricks(supported_by)
    print(amount_desintegratable.count(True))


def task2(input_lines: list[str]):
    x_max, y_max, z_max, blocks = parse_blocks(input_lines)
    supported_by = drop_and_find_supporters(x_max, y_max, z_max, blocks)
    chain_reaction_count = sum_of_chain_reaction(supported_by)
    print(chain_reaction_count)


def build_3d_array(x_max: int, y_max: int, z_max: int, fill_with: Any) -> list[list[list[Any]]]:
    result = []
    for _ in range(x_max):
        x_list = []
        for _ in range(y_max):
            y_list = []
            for _ in range(z_max):
                y_list.append(fill_with)
            x_list.append(y_list)
        result.append(x_list)
    return result


# x_max, y_max, z_max, blocks[start, end]
def parse_blocks(lines: list[str]) -> tuple[int, int, int, list[tuple[int, tuple[int, int, int], tuple[int, int, int]]]]:
    x_max = 0
    y_max = 0
    z_max = 0
    blocks = []

    for idx, block in enumerate(lines):
        start = tuple([int(x) for x in block.split("~")[0].split(",")])
        end = tuple([int(x) for x in block.split("~")[1].split(",")])
        
        block_x_min, block_x_max = min(start[0], end[0]), max(start[0], end[0])
        block_y_min, block_y_max = min(start[1], end[1]), max(start[1], end[1])
        block_z_min, block_z_max = min(start[2], end[2]), max(start[2], end[2])

        x_max = max(x_max, block_x_max)
        y_max = max(y_max, block_y_max)
        z_max = max(z_max, block_z_max)

        blocks.append((idx, (block_x_min, block_y_min, block_z_min), (block_x_max, block_y_max, block_z_max)))
    
    return x_max+1, y_max+1, z_max+1, blocks

def drop_and_find_supporters(x_max: int, y_max: int, z_max: int, blocks: list[tuple[int, tuple[int, int, int], tuple[int, int, int]]]):
    containing_grid = build_3d_array(x_max, y_max, z_max, None)
    supported_by = [[] for _ in blocks]

    sorted_blocks = sorted(blocks, key=lambda x: min(x[1][2],x[2][2]))

    for i in range(len(sorted_blocks)):
        print(f"Working on block {i}")
        brick_id, brick_start, brick_end = sorted_blocks[i]
        supported = []

        # Figuring out min z and supporting blocks
        should_continue = True
        z_min = brick_start[2]+1
        while should_continue and z_min >= 1:
            z_min -= 1
            should_continue = True

            for x in range(brick_start[0], brick_end[0]+1):
                for y in range(brick_start[1], brick_end[1]+1):
                    if containing_grid[x][y][z_min] == None:
                        continue
                    else:
                        should_continue = False
                        support = containing_grid[x][y][z_min]
                        if support not in supported:
                            supported.append(support)

        # Placing the block in the minimal location
        for x in range(brick_start[0], brick_end[0]+1):
            for y in range(brick_start[1], brick_end[1]+1):
                for z in range(z_min+1, z_min + (brick_end[2] - brick_start[2]) + 2):
                    containing_grid[x][y][z] = brick_id
        supported_by[brick_id] = supported

    return supported_by

def find_desintegratable_bricks(supported_by: list[list[int]]):
    desintegratable = [True for _ in supported_by]

    for brick in supported_by:
        if len(brick) != 1:
            continue
        for supporter in brick:
            desintegratable[supporter] = False
    return desintegratable

def sum_of_chain_reaction(supported_by: list[list[int]]):
    result = 0
    for destroyable_idx in range(len(supported_by)):
        destroyed = []
        next_iter = [destroyable_idx]
        while len(next_iter) != 0:
            destroyed.extend(next_iter)
            next_iter.clear()
            for idx, brick in enumerate(supported_by):
                if idx in destroyed:
                    continue
                dropping = True
                can_drop = False
                for supporter in brick:
                    if supporter not in destroyed:
                        dropping = False
                        break
                    else:
                        can_drop = True
                if dropping and can_drop:
                    next_iter.append(idx)
        print(f"Brick {destroyable_idx} would result in drop of {len(destroyed) - 1} bricks")
        result += len(destroyed) - 1
    return result