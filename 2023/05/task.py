import re

def task1(input_lines: list[str]):
    seeds_line = re.compile(r"seeds: ([\d ]*)").match(input_lines.pop(0))
    seeds = [int(x) for x in seeds_line.group(1).split()]
    input_lines.pop(0)
    print(seeds)
    transform = transform_next(input_lines, seeds)
    print(transform)
    print(min(transform))

def task2(input_lines: list[str]):
    seeds_line = re.compile(r"seeds: ([\d ]*)").match(input_lines.pop(0))
    seed_ranges = [int(x) for x in seeds_line.group(1).split()]
    seeds = []
    for r in range(0, len(seed_ranges), 2):
        seeds.append((seed_ranges[r], seed_ranges[r+1]))
    input_lines.pop(0)
    print(seeds)
    transform = transform_next_range(input_lines, seeds)
    print(transform)
    start_values =  [x[0] for x in transform]
    print(min(start_values))


def transform_next(lines: list[str], previous_list: list[int]):
    lines.pop(0) # header
    new_list = previous_list
    already_transformed = [False for _ in previous_list]
    while len(lines) > 0:
        l = lines.pop(0)
        if l == "":
            break
        parsed_line = re.compile(r"(\d*) (\d*) (\d*)").match(l)
        for idx in range(len(previous_list)):
            if already_transformed[idx]:
                continue
            prev = previous_list[idx]
            if prev >= int(parsed_line.group(2)) and prev < int(parsed_line.group(2)) + int(parsed_line.group(3)):
                offset = prev - int(parsed_line.group(2))
                new = int(parsed_line.group(1)) + offset
                new_list[idx] = new
                already_transformed[idx] = True
    print(new_list)
    if len(lines) > 0:
        return transform_next(lines, new_list)
    else:
        return new_list



def transform_next_range(lines: list[str], previous_list: list[(int, int)]) -> list[(int, int)]:
    lines.pop(0) # header
    new_list = []
    next_iteration = previous_list
    while len(lines) > 0:
        l = lines.pop(0)
        if l == "":
            break
        parsed_line = re.compile(r"(\d*) (\d*) (\d*)").match(l)
        to_iterate = next_iteration
        next_iteration = []
        while len(to_iterate) > 0:
            range_start, range_len = to_iterate.pop(0)

            line_src_range_start = int(parsed_line.group(2))
            line_dst_range_start = int(parsed_line.group(1))
            line_range_len = int(parsed_line.group(3))
            line_src_range_end = line_src_range_start + line_range_len - 1
            line_dst_range_end = line_dst_range_start + line_range_len - 1

            range_end = range_start + range_len - 1

            if range_end < line_src_range_end and range_start >= line_src_range_start:
                # Contained completely
                offset = range_start - line_src_range_start
                new_start = line_dst_range_start + offset
                new_list.append((new_start, range_len))
            elif range_end >= line_src_range_end and range_start < line_src_range_end:
                # Start contained
                offset = range_start - line_src_range_start
                new_start_one = line_dst_range_start + offset
                new_start_two = line_src_range_end + 1
                new_len_one = line_dst_range_end - new_start_one + 1
                new_len_two = range_len - new_len_one
                if new_len_one <= 0:
                    print("ALARM - start contained, len one")
                if new_len_two > 0:
                    next_iteration.append((new_start_two, new_len_two))
                elif new_len_two < 0:
                    print("ALARM - start contained, len two")
                new_list.append((new_start_one, new_len_one))
                if new_len_one + new_len_two != range_len:
                    print("ALARM - start, range")
            elif range_end >= line_src_range_start and range_start <= line_src_range_start:
                # End contained
                new_start_one = line_dst_range_start
                new_len_one = range_end - line_src_range_start + 1
                new_start_two = range_start
                new_len_two = range_len - new_len_one
                new_list.append((new_start_one, new_len_one))
                next_iteration.append((new_start_two, new_len_two))
                if new_len_one <= 0:
                    print("ALARM - end contained, len one")
                if new_len_two <= 0:
                    print("ALARM - end contained, len two")
                if new_len_one + new_len_two != range_len:
                    print("ALARM - end, range")
            elif range_end > line_src_range_end and range_start <= line_src_range_start:
                # Contained in middle
                new_start_one = range_start
                new_len_one = line_src_range_start - new_start_one
                new_start_two = line_src_range_end + 1
                new_len_two = range_end - new_start_two
                new_start_three = line_dst_range_start
                new_len_three = line_range_len

                new_list.append((new_start_three, new_len_three))
                next_iteration.append((new_start_one, new_len_one))
                next_iteration.append((new_start_two, new_len_two))

                if new_len_one + new_len_two + new_len_three != range_len:
                    print("ALARM - middle, range")

                if new_len_one <= 0:
                    print("ALARM - middle, len one")
                if new_len_two <= 0:
                    print("ALARM - middle, len two")
                if new_len_three <= 0:
                    print("ALARM - middle, len three")

            else:
                next_iteration.append((range_start, range_len))
    new_list.extend(next_iteration)

    if len(lines) > 0:
        return transform_next_range(lines, new_list)
    else:
        return new_list
