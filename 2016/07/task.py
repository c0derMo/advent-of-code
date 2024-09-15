def task1(input_lines: list[str]):
    passing = 0
    for line in input_lines:
        if supports_tls(line):
            print(f"Supporting: {line}")
            passing += 1
    print(passing)

def task2(input_lines: list[str]):
    passing = 0
    for line in input_lines:
        if supports_ssl(line):
            # print(f"Supporting: {line}")
            passing += 1
    print(passing)

def supports_tls(checking: str) -> bool:
    opened_brackets = 0
    has_abba = False
    for i in range(len(checking) - 3):
        if checking[i] == "[":
            opened_brackets += 1
        elif checking[i] == "]":
            opened_brackets -= 1
        if checking[i] == checking[i+3] and checking[i+1] == checking[i+2] and checking[i] != checking[i+1]:
            if opened_brackets >= 1:
                return False
            else:
                has_abba = True
    return has_abba

def supports_ssl(checking: str) -> bool:
    inside_brackets = False
    abas = []
    babs = []
    for i in range(len(checking) - 2):
        if checking[i] == "[":
            inside_brackets = True
        elif checking[i] == "]":
            inside_brackets = False
        elif checking[i] == checking[i+2] and checking[i] != checking[i+1]:
            if inside_brackets:
                babs.append(checking[i:i+3])
                corresponding_aba = checking[i+1] + checking[i] + checking[i+1]
                if corresponding_aba in abas:
                    return True
            else:
                abas.append(checking[i:i+3])
                corresponding_bab = checking[i+1] + checking[i] + checking[i+1]
                if corresponding_bab in babs:
                    return True
    return False