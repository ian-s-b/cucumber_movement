from pathlib import Path

from cucumbers_gif_maker.cucumbers_gif_maker import CucumbersGifMaker
from cucumbers_mover.cucumbers_mover import CucumbersMover

cucumbers_mover = CucumbersMover(Path("inputs/input_small.txt"))

print("Number of frames till equilibrium position: ", cucumbers_mover.get_last_frame_number)

gif_maker = CucumbersGifMaker(cucumbers_mover.get_frames, Path("outputs"))

images_paths = gif_maker.make_images()

gif_maker.make_gif(Path("outputs/animation.gif"), images_paths)
