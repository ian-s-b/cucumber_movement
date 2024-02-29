from copy import deepcopy
from pathlib import Path
from typing import Optional


class CucumbersMover:
    def __init__(self, input_file: Path, store_frames=True, stop_frame_number=1000):
        self._initial_positions = self._get_cucumbers_initial_positions(input_file)
        self._stop_frame_number = stop_frame_number
        self._frame_number = 0
        self._store_frames = store_frames
        self._move_till_equilibrium()
        self._all_frames = []

    @staticmethod
    def _get_cucumbers_initial_positions(input_file: Path):
        with open(input_file, "r", encoding="utf-8") as f:
            return [[j for j in i.strip()] for i in f.readlines()]

    @staticmethod
    def _is_occupied(position):
        return True if position == ">" or position == "v" else False

    def _move_cucumbers(self, positions):
        # Move cucumbers right
        positions_after_right_move = deepcopy(positions)

        for i, row in enumerate(positions):
            for j, position in enumerate(row):
                j_right = (j+1) % len(row)
                if position == ">" and not self._is_occupied(positions[i][j_right]):
                    positions_after_right_move[i][j] = "."
                    positions_after_right_move[i][j_right] = ">"

        # Move cucumbers down
        positions_after_down_move = deepcopy(positions_after_right_move)

        for i, row in enumerate(positions_after_right_move):
            for j, position in enumerate(row):
                i_down = (i+1) % len(positions_after_right_move)
                if position == "v" and not self._is_occupied(positions_after_right_move[i_down][j]):
                    positions_after_down_move[i][j] = "."
                    positions_after_down_move[i_down][j] = "v"

        return positions_after_down_move

    def _move_till_equilibrium(self):
        actual_positions = self._initial_positions
        has_moved = True

        while has_moved and self._frame_number < self._stop_frame_number:
            position_after_moving = self._move_cucumbers(actual_positions)

            has_moved = False

            for i, row in enumerate(actual_positions):
                if "".join(row) != "".join(position_after_moving[i]):
                    has_moved = True
                    break

            actual_positions = position_after_moving
            self._frame_number += 1

    @property
    def get_last_frame(self):
        return self._frame_number

    @property
    def get_all_frames(self) -> Optional[list[str]]:
        return self._all_frames
