from functools import cmp_to_key

def task1(input_lines: list[str]):
    hands: list[tuple[str, int]] = []
    for line in input_lines:
        hands.append((line.split()[0], int(line.split()[1])))
    
    sorted_hands = sorted(hands, key=cmp_to_key(compare_hands), reverse=True)

    print(sorted_hands)
    result = 0
    for idx, hand in enumerate(sorted_hands):
        result += hand[1] * (idx + 1)
    print(result)


def task2(input_lines: list[str]):
    hands: list[tuple[str, int]] = []
    for line in input_lines:
        hands.append((line.split()[0], int(line.split()[1])))
    
    sorted_hands = sorted(hands, key=cmp_to_key(compare_hands_with_jokers), reverse=True)

    # print(sorted_hands)
    result = 0
    for idx, hand in enumerate(sorted_hands):
        result += hand[1] * (idx + 1)
    print(result)


def compare_hands_with_jokers(hand_one: tuple[str, int], hand_two: tuple[str, int]) -> int:
    hand_one_rank = get_hand_rank(hand_one[0], True)
    hand_two_rank = get_hand_rank(hand_two[0], True)
    if hand_one_rank != hand_two_rank:
        return hand_two_rank - hand_one_rank
    
    card_one_rank = get_card_rank(hand_one[0][0], True)
    card_two_rank = get_card_rank(hand_two[0][0], True)
    next_card = 1
    while card_one_rank == card_two_rank:
        card_one_rank = get_card_rank(hand_one[0][next_card], True)
        card_two_rank = get_card_rank(hand_two[0][next_card], True)
        next_card += 1
    return card_one_rank - card_two_rank

def compare_hands(hand_one: tuple[str, int], hand_two: tuple[str, int]) -> int:
    hand_one_rank = get_hand_rank(hand_one[0])
    hand_two_rank = get_hand_rank(hand_two[0])
    if hand_one_rank != hand_two_rank:
        return hand_two_rank - hand_one_rank
    
    card_one_rank = get_card_rank(hand_one[0][0])
    card_two_rank = get_card_rank(hand_two[0][0])
    next_card = 1
    while card_one_rank == card_two_rank:
        card_one_rank = get_card_rank(hand_one[0][next_card])
        card_two_rank = get_card_rank(hand_two[0][next_card])
        next_card += 1
    return card_one_rank - card_two_rank


def get_card_rank(card: str, jokers=False) -> int:
    if jokers:
        return ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"].index(card)
    else:
        return ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"].index(card)


def max_without_jokers(char_amounts: dict[str, int]) -> int:
    m = 0
    for k, v in char_amounts.items():
        if k == "J":
            continue
        if v > m:
            m = v
    return m


def get_hand_rank(hand: str, jokers=False) -> int:
    char_amounts = get_character_amounts(hand)
    if max(char_amounts.values()) == 5 or (jokers and "J" in char_amounts.keys() and max_without_jokers(char_amounts) + char_amounts["J"] == 5):
        return 7
    if max(char_amounts.values()) == 4 or (jokers and "J" in char_amounts.keys() and max_without_jokers(char_amounts) + char_amounts["J"] == 4):
        return 6
    if (3 in char_amounts.values() and 2 in char_amounts.values())  or (jokers and "J" in char_amounts.keys() and len(char_amounts.keys()) == 3):
        return 5
    if max(char_amounts.values()) == 3 or (jokers and "J" in char_amounts and max_without_jokers(char_amounts) + char_amounts["J"] == 3):
        return 4
    
    amount_pairs = 0
    if jokers:
        jokers_used = 0
        jokers_total = 0
        if "J" in char_amounts:
            jokers_total = char_amounts["J"]
        for k, v in char_amounts.items():
            if k == "J":
                continue
            if v == 2:
                amount_pairs += 1
            if v == 1 and jokers_total - jokers_used >= 1:
                amount_pairs += 1
                jokers_used += 1
    else:
        for i in char_amounts.values():
            if i == 2:
                amount_pairs += 1
    if amount_pairs == 2:
        return 3
    if amount_pairs == 1:
        return 2
    
    return 1


def get_character_amounts(hand: str) -> dict[str, int]:
    result = {}
    for char in hand:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result