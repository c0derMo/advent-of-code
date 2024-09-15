def task1(input_lines: list[str]):
    pw_len = len(input_lines[0])
    character_occurances = [({}) for _ in range(pw_len)]

    for line in input_lines:
        for idx, char in enumerate(line):
            if char not in character_occurances[idx]:
                character_occurances[idx][char] = 0
            character_occurances[idx][char] += 1
    

    pw = ""
    for i in range(pw_len):
        most_common_char = ""
        for key in character_occurances[i].keys():
            if most_common_char == "" or character_occurances[i][key] > character_occurances[i][most_common_char]:
                most_common_char = key
        pw += most_common_char
    print(pw)

def task2(input_lines: list[str]):
    pw_len = len(input_lines[0])
    character_occurances = [({}) for _ in range(pw_len)]

    for line in input_lines:
        for idx, char in enumerate(line):
            if char not in character_occurances[idx]:
                character_occurances[idx][char] = 0
            character_occurances[idx][char] += 1
    

    pw = ""
    for i in range(pw_len):
        least_common_char = ""
        for key in character_occurances[i].keys():
            if least_common_char == "" or character_occurances[i][key] < character_occurances[i][least_common_char]:
                least_common_char = key
        pw += least_common_char
    print(pw)