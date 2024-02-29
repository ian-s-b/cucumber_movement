from pathlib import Path

from cucumbers_mover.cucumbers_mover import CucumbersMover

cucumbers_mover = CucumbersMover(Path("inputs/input_big.txt"))

print(cucumbers_mover.get_last_frame)
