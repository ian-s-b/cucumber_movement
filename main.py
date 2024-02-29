from pathlib import Path

from cucumbers_mover.cucumbers_mover import CucumbersMover

cucumbers_mover = CucumbersMover()

init_pos = cucumbers_mover.get_cucumbers_initial_positions(Path("inputs/input_big.txt"))

equilibrium_frame = cucumbers_mover.get_equilibrium_frame(init_pos)

print(equilibrium_frame)