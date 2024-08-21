def task1(input_lines: list[str]):
    start_string, replacements = parse_file(input_lines)
    # print(replacements)
    print(f"Found {len(replacements)} replacements. Start string:")
    print(start_string)
    options = try_replace(start_string, replacements)
    print(f"Found {len(options)} different results:")
    # print(options)
    print(len(options))


def task2(input_lines: list[str]):
    start_string, replacements = parse_file(input_lines, True)
    target = "e"

    open_options: list[tuple[str, int]] = [(start_string, 0)]
    all_options = set()
    while len(open_options) > 0:
        current_option = open_options.pop(0)
        print(current_option[0])

        if current_option[0] == target:
            print(current_option[1])
            break

        single_replacement_options = try_replace(current_option[0], replacements)
        for option in single_replacement_options:
            if option in all_options:
                continue
            else:
                all_options.add(option)
                open_options.append((option, current_option[1]+1))
        open_options.sort(key=lambda x: len(x[0]))


def parse_file(input_file: list[str], reverse = False) -> tuple[str, list[tuple[str, str]]]:
    replacements = []
    start_string = ""
    next_is_start = False
    for line in input_file:
        if line == "":
            next_is_start = True
        elif next_is_start:
            start_string = line
        else:
            splitted = line.split(" => ")
            if reverse:
                replacements.append(tuple([splitted[1], splitted[0]]))
            else:
                replacements.append(tuple([splitted[0], splitted[1]]))
    return start_string, replacements

def try_replace(input_string: str, replacements: list[tuple[str, str]], reverse = False) -> set[str]:
    result = set()

    for replacement in replacements:
        if reverse:
            i = len(input_string)
        else:
            i = 0
        while (i <= len(input_string) and not reverse) or (i >= 0 and reverse):
            possible_index = input_string.find(replacement[0], i)
            if possible_index == -1:
                i += 1
            else:
                new_string = input_string[:possible_index] + replacement[1] + input_string[possible_index+len(replacement[0]):]
                result.add(new_string)
                i += len(replacement[0])
    return result