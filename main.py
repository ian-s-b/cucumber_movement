from pathlib import Path

from cucumbers_mover.cucumbers_mover import CucumbersMover

cucumbers_mover = CucumbersMover(Path("inputs/input_big.txt"))

equilibrium_frame = cucumbers_mover.get_equilibrium_frame()

print(equilibrium_frame)
