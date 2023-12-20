import math

def task1(input_lines: list[str]):
    gates, state = build_gates(input_lines)

    all_highs = 0
    all_lows = 0
    for _ in range(1000):
        highs, lows, state = single_button_push(gates, state)
        all_highs += highs
        all_lows += lows
    print(all_highs)
    print(all_lows)
    print(all_highs * all_lows)

def task2(input_lines: list[str]):
    gates, state = build_gates(input_lines)
    i = figure_out_rx_presses(gates, state)
    print(i)


def build_gates(lines: list[str]) -> tuple[dict[str, tuple[str, list[str]]], dict[str, dict[str, bool]]]:
    gates = {}
    initial_state = {}

    for line in lines:
        if line.startswith("&"):
            # Conjunctions
            name = line.split(" -> ")[0][1:]
            targets = line.split(" -> ")[1].split(", ")
            gates[name] = ("c", targets)
            initial_state[name] = {}

    for line in lines:
        if line.startswith("%"):
            # Flip-Flop
            name = line.split(" -> ")[0][1:]
            targets = line.split(" -> ")[1].split(", ")
            gates[name] = ("f", targets)
            initial_state[name] = {"state": False}
        if line.startswith("broadcaster"):
            # Broadcaster
            name = "broadcaster"
            targets = line.split(" -> ")[1].split(", ")
            gates[name] = ("b", targets)
        if line.startswith("&"):
            # Conjunction no2
            name = line.split(" -> ")[0][1:]
            targets = line.split(" -> ")[1].split(", ")
        
        for target in targets:
            if target in gates and gates[target][0] == "c":
                initial_state[target][name] = False
    return gates, initial_state


def figure_out_rx_presses(gates: dict[str, tuple[str, list[str]]], state: dict[str, dict[str, bool]]):
    new_state = state
    cycles = {}
    i = 0

    while True:
        i += 1
        pushes = [("button", "broadcaster", False)]
        while len(pushes) != 0:
            origin, target, high = pushes.pop(0)

            # print(f"{origin} -{'high' if high else 'low'}-> {target}")
            if target == "rx" and not high:
                return i
            if target == "cl" and high:
                if origin not in cycles:
                    cycles[origin] = i
                if cycles.keys() == state[target].keys():
                    # We got all cycles
                    all_cycles = [c for c in cycles.values()]
                    result = all_cycles.pop(0)
                    for cycle in all_cycles:
                        result *= cycle // math.gcd(cycle, result)
                    return result
                print(cycles)

            if target not in gates:
                continue

            gate_type, gate_targets = gates[target]
            if gate_type == "b":
                for send_target in gate_targets:
                    pushes.append((target, send_target, high))
            if gate_type == "f" and not high:
                new_state[target]["state"] = not new_state[target]["state"]
                for send_target in gate_targets:
                    pushes.append((target, send_target, new_state[target]["state"]))
            if gate_type == "c":
                new_state[target][origin] = high
                # print(new_state[target])
                if all(new_state[target].values()):
                    for send_target in gate_targets:
                        pushes.append((target, send_target, False))
                else:
                    for send_target in gate_targets:
                        pushes.append((target, send_target, True))


def single_button_push(gates: dict[str, tuple[str, list[str]]], state: dict[str, dict[str, bool]]):
    new_state = state
    pushes = [("button", "broadcaster", False)]

    low_pulses = 0
    high_pulses = 0

    while len(pushes) != 0:
        origin, target, high = pushes.pop(0)

        # print(f"{origin} -{'high' if high else 'low'}-> {target}")
        if high:
            high_pulses += 1
        else:
            low_pulses += 1

        if target not in gates:
            continue

        gate_type, gate_targets = gates[target]
        if gate_type == "b":
            for send_target in gate_targets:
                pushes.append((target, send_target, high))
        if gate_type == "f" and not high:
            new_state[target]["state"] = not new_state[target]["state"]
            for send_target in gate_targets:
                pushes.append((target, send_target, new_state[target]["state"]))
        if gate_type == "c":
            new_state[target][origin] = high
            # print(new_state[target])
            if all(new_state[target].values()):
                for send_target in gate_targets:
                    pushes.append((target, send_target, False))
            else:
                for send_target in gate_targets:
                    pushes.append((target, send_target, True))
    
    return high_pulses, low_pulses, new_state