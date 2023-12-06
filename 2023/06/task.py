import math

def task1(input_lines: list[str]):
    time = input_lines[0].split()
    distance = input_lines[1].split()

    result = 1

    for i in range(1, len(time)):
        ways_to_win = get_ways_to_win(int(time[i]), int(distance[i]))
        print(f"Race {i}: {ways_to_win}")
        result *= ways_to_win
    
    print(result)

def task2(input_lines: list[str]):
    time = input_lines[0].split()
    distance = input_lines[1].split()

    total_time = int("".join(time[1:]))
    total_distance = int("".join(distance[1:]))

    print(total_time)
    print(total_distance)

    # Not necessarily the most optimal way, but took ~2s, so it worked imo
    ways_to_win = get_ways_to_win(total_time, total_distance)
    print(ways_to_win)




def get_ways_to_win(time: int, distance_needed: int) -> int:
    current_charge_time = math.floor(time / 2)
    
    ways_to_win = 1
    if (time / 2) % 1 != 0:
        ways_to_win += 1
    
    while True:
        current_charge_time -= 1
        if current_charge_time * (time - current_charge_time) > distance_needed:
            ways_to_win += 2
        else:
            break
    
    return ways_to_win