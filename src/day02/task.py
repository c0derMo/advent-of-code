SCORE_ROCK = 1
SCORE_PAPER = 2
SCORE_SCISSOR = 3

SCORE_WIN = 6
SCORE_DRAW = 3
SCORE_LOSE = 0

def task1(inputLines):
    score = 0
    for line in inputLines:
        our_symbol = line[2:]
        their_symbol = line[:1]
        if our_symbol == "X":
            if their_symbol == "A":
                # Rock v Rock
                score += SCORE_ROCK + SCORE_DRAW
            elif their_symbol == "B":
                # Rock v Paper
                score += SCORE_ROCK + SCORE_LOSE
            elif their_symbol == "C":
                # Rock v Scissor
                score += SCORE_ROCK + SCORE_WIN
            else:
                print("Our opponent has an invalid symbol: " + their_symbol)
        elif our_symbol == "Y":
            if their_symbol == "A":
                # Paper v Rock
                score += SCORE_PAPER + SCORE_WIN
            elif their_symbol == "B":
                # Paper v Paper
                score += SCORE_PAPER + SCORE_DRAW
            elif their_symbol == "C":
                # Paper v Scissor
                score += SCORE_PAPER + SCORE_LOSE
            else:
                print("Our opponent has an invalid symbol: " + their_symbol)
        elif our_symbol == "Z":
            if their_symbol == "A":
                # Scissor v Rock
                score += SCORE_SCISSOR + SCORE_LOSE
            elif their_symbol == "B":
                # Scissors v Paper
                score += SCORE_SCISSOR + SCORE_WIN
            elif their_symbol == "C":
                # Scissors v Scissor
                score += SCORE_SCISSOR + SCORE_DRAW
            else:
                print("Our opponent has an invalid symbol: " + their_symbol)
        else:
            print("We have an invalid symbol: " + our_symbol)

    print("Total score: " + str(score))

def task2(inputLines):
    score = 0
    for line in inputLines:
        our_symbol = line[2:]
        their_symbol = line[:1]
        if our_symbol == "X":
            if their_symbol == "A":
                # Lose v Rock
                score += SCORE_SCISSOR + SCORE_LOSE
            elif their_symbol == "B":
                # Lose v Paper
                score += SCORE_ROCK + SCORE_LOSE
            elif their_symbol == "C":
                # Lose v Scissor
                score += SCORE_PAPER + SCORE_LOSE
            else:
                print("Our opponent has an invalid symbol: " + their_symbol)
        elif our_symbol == "Y":
            if their_symbol == "A":
                # Draw v Rock
                score += SCORE_ROCK + SCORE_DRAW
            elif their_symbol == "B":
                # Draw v Paper
                score += SCORE_PAPER + SCORE_DRAW
            elif their_symbol == "C":
                # Draw v Scissor
                score += SCORE_SCISSOR + SCORE_DRAW
            else:
                print("Our opponent has an invalid symbol: " + their_symbol)
        elif our_symbol == "Z":
            if their_symbol == "A":
                # Win v Rock
                score += SCORE_PAPER + SCORE_WIN
            elif their_symbol == "B":
                # Win v Paper
                score += SCORE_SCISSOR + SCORE_WIN
            elif their_symbol == "C":
                # Win v Scissor
                score += SCORE_ROCK + SCORE_WIN
            else:
                print("Our opponent has an invalid symbol: " + their_symbol)
        else:
            print("We have an invalid symbol: " + our_symbol)

    print("Total score: " + str(score))
