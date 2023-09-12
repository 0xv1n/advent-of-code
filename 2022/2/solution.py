import os

with open(os.path.dirname(__file__) + "/input.txt") as f:
    input = f.readlines()

# Rules of Rock, Paper, Scissors:
# - Rock beats Scissors
# - Scissors beats Paper
# - Paper Beats Rock

# Rock Paper Scissors Key
# Column 1 | Column 2
#   A | X = Rock
#   B | Y = Paper
#   C | Z = Scissor

# Scoring
shape_score = {"X": 1, "Y": 2, "Z": 3}
outcome_score = {"lost": 0, "draw": 3, "won": 6}
shapes = {"A": "X", "B": "Y", "C": "Z"}


def calculate_score(shape, outcome):
    return shape_score[shape] + outcome_score[outcome]


def determine_winner(opponent, my_move):
    if shapes[opponent] == my_move:
        return "draw"
    # opponent chose Rock
    elif opponent == "A":
        return "won" if my_move == "Y" else "lost"
    # opponent chose Paper
    elif opponent == "B":
        return "won" if my_move == "Z" else "lost"
    # opponent chose Scissor
    elif opponent == "C":
        return "won" if my_move == "X" else "lost"


def main():
    total_score = 0
    for line in input:
        result = determine_winner(opponent=line.split()[0], my_move=line.split()[1])
        total_score += calculate_score(line.split()[1], result)
    print(total_score)


if __name__ == "__main__":
    main()
