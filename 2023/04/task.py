import re

def task1(input_lines: list[str]):
    result = 0
    for idx, game in enumerate(input_lines):
        score = card_score(game)
        print(f"Game {idx+1} -> {score}")
        result += score
    print(result)

def task2(input_lines: list[str]):
    card_counts = [1 for _ in input_lines]
    for idx, game in enumerate(input_lines):
        score = card_score_sum(game)
        print(f"Card {idx+1} * {card_counts[idx]} -> {score}")
        while score > 0:
            card_counts[idx + score] += card_counts[idx]
            score -= 1
    print(sum(card_counts))


def card_score(card: str) -> int:
    parsed = re.compile(r"Card ([\d ]+): ([\d ]+) \| ([\d ]+)").match(card)
    if parsed == None:
        raise AttributeError("Card couldnt get parsed")
    
    game_id = int(parsed.group(1))
    winning = [int(x) for x in parsed.group(2).split()]
    own = [int(x) for x in parsed.group(3).split()]

    score = 0

    for num in own:
        if num in winning:
            if score == 0:
                score = 1
            else:
                score *= 2
    
    return score

def card_score_sum(card: str) -> int:
    parsed = re.compile(r"Card ([\d ]+): ([\d ]+) \| ([\d ]+)").match(card)
    if parsed == None:
        raise AttributeError("Card couldnt get parsed")
    
    game_id = int(parsed.group(1))
    winning = [int(x) for x in parsed.group(2).split()]
    own = [int(x) for x in parsed.group(3).split()]

    score = 0

    for num in own:
        if num in winning:
            score += 1
    
    return score