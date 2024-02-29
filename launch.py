from copy import deepcopy

input_lines = []

with open("input_2.txt", "r", encoding="utf-8") as f:
    input_lines = [[j for j in i.strip()] for i in f.readlines()]


# v...>>.vv>
# .vv>>.vv..
# >>.>v>...v
# >>v>>.>.v.
# v>v.vv.v..
# >.>>..v...
# .vv..>.>v.
# v.v..>>v.v
# ....v..v.>
    


def is_occupied(pos):
    if pos == ">" or pos == "v":
        return True
    return False


def move(input_lines):
    output_lines = deepcopy(input_lines)

    # RIGHT
    for idx_line, input_line in enumerate(input_lines):
        for idx_pos, pos in enumerate(input_line):
            right_idx = (idx_pos+1) % len(input_line)
            if pos == ">" and not is_occupied(input_lines[idx_line][right_idx]):
                output_lines[idx_line][idx_pos] = "."
                output_lines[idx_line][right_idx] = ">"
    
    output_lines_2 = deepcopy(output_lines)
    # DOWN
    for idx_line, output_line in enumerate(output_lines):
        for idx_pos, pos in enumerate(output_line):
            down_idx = (idx_line+1) % len(output_lines)
            if pos == "v" and not is_occupied(output_lines[down_idx][idx_pos]):
                output_lines_2[idx_line][idx_pos] = "."
                output_lines_2[down_idx][idx_pos] = "v"

    return output_lines_2


has_moved = True
all_time = 0

while has_moved and all_time < 100:
    print(all_time)
    output_lines = move(input_lines)
    
    has_moved = False

    for idx_line, input_line in enumerate(input_lines):
        if "".join(input_line) != "".join(output_lines[idx_line]):
            has_moved = True
            break

    output_lines = input_lines
    
    all_time += 1


print(all_time)

# o_lines = move(input_lines)

# for i in o_lines:
#     print(i)