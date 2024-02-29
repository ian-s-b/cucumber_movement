from copy import deepcopy


def get_cucumbers_initial_positions(input_file):
    with open(input_file, "r", encoding="utf-8") as f:
        return [[j for j in i.strip()] for i in f.readlines()]


def is_occupied(position):
    return True if position == ">" or position == "v" else False


def move_cucumbers(initial_positions):
    # Move cucumbers right
    positions_after_right_move = deepcopy(initial_positions)

    for i, row in enumerate(initial_positions):
        for j, position in enumerate(row):
            j_right = (j+1) % len(row)
            if position == ">" and not is_occupied(initial_positions[i][j_right]):
                positions_after_right_move[i][j] = "."
                positions_after_right_move[i][j_right] = ">"

    # Move cucumbers down
    positions_after_down_move = deepcopy(positions_after_right_move)

    for i, row in enumerate(positions_after_right_move):
        for j, position in enumerate(row):
            i_down = (i+1) % len(positions_after_right_move)
            if position == "v" and not is_occupied(positions_after_right_move[i_down][j]):
                positions_after_down_move[i][j] = "."
                positions_after_down_move[i_down][j] = "v"

    return positions_after_down_move


def get_cucumbers_equilibrium_position_frame(initial_positions, stop_frame=1000):

    actual_positions = initial_positions
    has_moved = True
    frame = 0

    while has_moved and frame < stop_frame:
        position_after_moving = move_cucumbers(actual_positions)

        has_moved = False

        for i, row in enumerate(actual_positions):
            if "".join(row) != "".join(position_after_moving[i]):
                has_moved = True
                break

        actual_positions = position_after_moving
        frame += 1

    return frame


initial_positions = get_cucumbers_initial_positions("input.txt")

equilibrium_frame = get_cucumbers_equilibrium_position_frame(initial_positions)

print(equilibrium_frame)
