from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

@dataclass
class FrameSize:
    nb_of_rows: int
    nb_of_cols: int

class CucumbersMover:
    def __init__(self, input_file: Path, save_frames=True, stop_frame_number=1000):
        self._initial_positions, self._frame_size = self._get_cucumbers_initial_positions(input_file)
        self._stop_frame_number = stop_frame_number
        self._frame_number = 0
        self._save_frames = save_frames
        self._frames = []
        self._move_till_equilibrium()


    def _get_cucumbers_initial_positions(self, input_file: Path):
        with open(input_file, "r", encoding="utf-8") as f:
            initial_positions = [[j for j in i.strip()] for i in f.readlines()]
            frame_size = FrameSize(nb_of_rows=len(initial_positions), nb_of_cols=len(initial_positions[0]))
            return initial_positions, frame_size

    @staticmethod
    def _is_occupied(position: str):
        return True if position == ">" or position == "v" else False

    def _move_cucumbers(self, positions: list[list[str]]) -> list[list[str]]:
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


    def _move_till_equilibrium(self) -> None:
        actual_positions = self._initial_positions
        has_moved = True

        while has_moved and self._frame_number < self._stop_frame_number:
            position_after_moving = self._move_cucumbers(actual_positions)
            has_moved = False
            frame = ""

            for i, row in enumerate(actual_positions):
                frame_row = " ".join(position_after_moving[i])

                if self._save_frames:
                    frame += frame_row + "\n"

                if " ".join(row) != frame_row:
                    has_moved = True
                    if not self._save_frames:
                        break

            self._frames.append(frame)
            actual_positions = position_after_moving
            self._frame_number += 1

    @property
    def get_last_frame_number(self) -> int:
        return self._frame_number

    @property
    def get_frames(self) -> Optional[list[str]]:
        return self._frames

    @property
    def get_frame_size(self) -> FrameSize:
        return self._frame_size
