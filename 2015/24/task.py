def task1(input_lines: list[str]):
    weights = [int(x) for x in input_lines]

    sum_per_compartment = sum(weights) / 3

    options = get_options_to_sum_up_to(weights, sum_per_compartment)

    shortest_op = len(weights)
    for op in options:
        shortest_op = min(shortest_op, len(op))
    
    shortest_ops: list[list[int]] = []
    for op in options:
        if len(op) == shortest_op:
            shortest_ops.append(op)
    
    shortest_ops.sort(key=lambda x: product(x))
    print(product(shortest_ops[0]))

def task2(input_lines: list[str]):
    weights = [int(x) for x in input_lines]

    sum_per_compartment = sum(weights) / 4

    options = get_options_to_sum_up_to(weights, sum_per_compartment)

    shortest_op = len(weights)
    for op in options:
        shortest_op = min(shortest_op, len(op))
    
    shortest_ops: list[list[int]] = []
    for op in options:
        if len(op) == shortest_op:
            shortest_ops.append(op)
    
    shortest_ops.sort(key=lambda x: product(x))
    print(product(shortest_ops[0]))


def product(numbers: list[int]):
    if len(numbers) == 0:
        return 0
    p = 1
    for n in numbers:
        p *= n
    return p


def get_options_to_sum_up_to(numbers: list[int], target: int) -> list[list[int]]:
    options: list[list[int]] = []
    for (idx, num) in enumerate(numbers):
        if num < target:
            next_options = get_options_to_sum_up_to(numbers[(idx+1):], target-num)
            for op in next_options:
                total_op = [num]
                total_op.extend(op)
                options.append(total_op)
        elif num == target:
            options.append([num])
    return options