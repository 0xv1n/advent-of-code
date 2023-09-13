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


def cheat(opponent, my_move):
    if my_move == "X":  # X means you need to lose
        # print("My move was X, we need to lose.")
        losing_shape = {"A": "Z", "B": "X", "C": "Y"}
        return losing_shape[opponent]
    elif my_move == "Y":  # Y means you need to draw
        # print("My move was Y, force draw.")
        return shapes[opponent]
    else:  # Z means you need to win.
        # print("My move was Z, we force win")
        winning_shape = {"A": "Y", "B": "Z", "C": "X"}
        return winning_shape[opponent]


def main():
    total_score = 0
    # Part 1
    print("[+] Playing game normally\n")
    for line in input:
        result = determine_winner(opponent=line.split()[0], my_move=line.split()[1])
        total_score += calculate_score(line.split()[1], result)
    print(f"Final Score: {total_score}")
    total_score = 0
    # Part 2 - We cheat.
    print("\n[!] Playing game by cheating\n")
    for line in input:
        opponent = line.split()[0]
        my_move = line.split()[1]
        # print(f"Opponents move: {opponent} | My move: {my_move}")
        cheat_shape = cheat(opponent=opponent, my_move=my_move)
        # print(f"Original Move: {my_move} | New Move: {cheat_shape}")
        result = determine_winner(opponent, cheat_shape)
        total_score += calculate_score(cheat_shape, result)
    print(f"Final Score (while cheating): {total_score}")


if __name__ == "__main__":
    main()
