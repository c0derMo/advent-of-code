def task1(input_lines: list[str]):
    containers = [int(x) for x in input_lines]
    containers.sort(reverse=True)
    print(containers)

    target_amount = 150
    options = recursively_find_options(target_amount, containers)
    # print(options)
    print(len(options))

def task2(input_lines: list[str]):
    containers = [int(x) for x in input_lines]
    containers.sort(reverse=True)
    print(containers)

    target_amount = 150
    options = recursively_find_options(target_amount, containers)

    options_lens = [len(x) for x in options]
    min_containers = min(options_lens)
    options_with_that_amount_of_containers = list(filter(lambda x: len(x) == min_containers, options))

    # print(options)
    print(len(options_with_that_amount_of_containers))


def recursively_find_options(target: int, remaining_options: list[int]) -> list[list[int]]:
    options = []

    for i in range(len(remaining_options)):
        if remaining_options[i] > target:
            continue
        elif remaining_options[i] == target:
            options.append([remaining_options[i]])
        else:
            chosen_container = remaining_options[i]
            new_remaining_options = remaining_options[i+1:]
            more_options = recursively_find_options(target - chosen_container, new_remaining_options)
            for option in more_options:
                new_option = [chosen_container]
                new_option.extend(option)
                options.append(new_option)
    return options