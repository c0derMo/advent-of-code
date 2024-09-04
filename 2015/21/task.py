import math

def task1(input_lines: list[str]):
    boss_health = int(input_lines[0].split(": ")[1])
    boss_at = int(input_lines[1].split(": ")[1])
    boss_df = int(input_lines[2].split(": ")[1])

    print(f"Boss stats: {boss_health} health, {boss_at} ATK, {boss_df} DEF")

    shop_combinations = get_all_shop_combinations()
    print(f"Shop combinations: {len(shop_combinations)}")

    shop_combinations.sort(key=lambda x: x[2])
    shop_combinations.sort(key=lambda x: x[1])
    shop_combinations.sort(key=lambda x: x[0])

    filtered_combinations = []
    for (idx, combination) in enumerate(shop_combinations):
        if idx == 0:
            filtered_combinations.append(combination)
        elif combination[1] > shop_combinations[idx-1][1] or combination[2] > shop_combinations[idx-1][2]:
            filtered_combinations.append(combination)
    
    print(f"Filtered combinations: {len(filtered_combinations)}")

    for combination in filtered_combinations:
        if can_beat_boss(100, combination[1], combination[2], boss_health, boss_at, boss_df):
            print(combination[0])
            return

    print("We can never beat the boss :(")

def task2(input_lines: list[str]):
    boss_health = int(input_lines[0].split(": ")[1])
    boss_at = int(input_lines[1].split(": ")[1])
    boss_df = int(input_lines[2].split(": ")[1])

    print(f"Boss stats: {boss_health} health, {boss_at} ATK, {boss_df} DEF")

    shop_combinations = get_all_shop_combinations()
    print(f"Shop combinations: {len(shop_combinations)}")

    shop_combinations.sort(key=lambda x: x[0], reverse=True)

    for combination in shop_combinations:
        if not can_beat_boss(100, combination[1], combination[2], boss_health, boss_at, boss_df):
            print(combination[0])
            return

    print("We can always beat the boss :(")


def can_beat_boss(player_health: int, player_at: int, player_df: int, boss_health: int, boss_at: int, boss_df: int) -> bool:
    turns_to_kill_boss = math.ceil(boss_health / max(1, player_at - boss_df))
    turns_to_kill_player = math.ceil(player_health / max(1, boss_at - player_df))
    return turns_to_kill_boss <= turns_to_kill_player


def get_all_shop_combinations() -> list[tuple[int, int, int]]:
    weapons = [
        (8, 4),
        (10, 5),
        (25, 6),
        (40, 7),
        (74, 8)
    ]

    armors = [
        (0, 0),
        (13, 1),
        (31, 2),
        (53, 3),
        (75, 4),
        (102, 5)
    ]

    rings = [
        (0, 0, 0),
        (0, 0, 0),
        (25, 1, 0),
        (50, 2, 0),
        (100, 3, 0),
        (20, 0, 1),
        (40, 0, 2),
        (80, 0, 3),
    ]

    result = []

    for weapon in weapons:
        for armor in armors:
            for (idx, ring) in enumerate(rings):
                for ring2 in rings[(idx+1):]:
                    cost = weapon[0] + armor[0] + ring[0] + ring2[0]
                    at = weapon[1] + ring[1] + ring2[1]
                    df = armor[1] + ring[2] + ring2[2]
                    result.append(tuple([cost, at, df]))
    return result