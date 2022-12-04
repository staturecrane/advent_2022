from advent import utils

move_scores = {"X": 1, "Y": 2, "Z": 3}

moves_that_win = ["C X", "A Y", "B Z"]
moves_that_draw = ["A X", "B Y", "C Z"]

moves_that_draw_ = {"A": "X", "B": "Y", "C": "Z"}
moves_that_lose = {"A": "Z", "B": "X", "C": "Y"}
moves_that_win_ = {"A": "Y", "B": "Z", "C": "X"}


@utils.input_wrapper
def calculate_rps_rounds_part_one(input_data):
    scores = []

    for round in input_data:
        round = round.strip()
        player_a_move, player_b_move = round.split(" ")
        move_score = move_scores[player_b_move]

        if f"{player_a_move} {player_b_move}" in moves_that_draw:
            scores.append(move_score + 3)
        elif f"{player_a_move} {player_b_move}" in moves_that_win:
            scores.append(move_score + 6)
        else:
            scores.append(move_score)

    return sum(scores)


@utils.input_wrapper
def calculate_rps_rounds_part_two(input_data):
    scores = []

    for round in input_data:
        round = round.strip()
        player_a_move, player_b_move = round.split(" ")

        if player_b_move == "X":
            redrawn_move = moves_that_lose[player_a_move]
        elif player_b_move == "Y":
            redrawn_move = moves_that_draw_[player_a_move]
        else:
            redrawn_move = moves_that_win_[player_a_move]

        move_score = move_scores[redrawn_move]

        if f"{player_a_move} {redrawn_move}" in moves_that_draw:
            scores.append(move_score + 3)
        elif f"{player_a_move} {redrawn_move}" in moves_that_win:
            scores.append(move_score + 6)
        else:
            scores.append(move_score)

    return sum(scores)


if __name__ == "__main__":
    print(calculate_rps_rounds_part_one())
    print(calculate_rps_rounds_part_two())
