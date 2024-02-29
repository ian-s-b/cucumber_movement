import time
from pathlib import Path

from cucumbers_gif_maker.cucumbers_gif_maker import CucumbersGifMaker
from cucumbers_mover.cucumbers_mover import CucumbersMover

cucumbers_mover = CucumbersMover(Path("inputs/input_small.txt"))

print(cucumbers_mover.get_last_frame_number)

gif_maker = CucumbersGifMaker(cucumbers_mover.get_frames)

for frame_number, frame in enumerate(cucumbers_mover.get_frames):
    print(frame)
    print(f"Frame number: {frame_number}")
    time.sleep(0.2)