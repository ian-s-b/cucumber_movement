from pathlib import Path

import imageio
from PIL import Image, ImageDraw, ImageFont


class CucumbersGifMaker:
    def __init__(self, frames: list[str], output_path: Path):
        self._frames = frames
        self._output_path = output_path
        self._padding = 5

    def make_images(self):
        images_paths = []
        default_font = ImageFont.load_default()
        text_size = ImageDraw.Draw(Image.new('1', (1, 1))).textsize(
            self._frames[0], default_font)
        image_size = (text_size[0] + self._padding, text_size[1] + self._padding)

        for frame_number, frame in enumerate(self._frames):
            image = Image.new(mode='1', size=image_size, color=1)
            draw = ImageDraw.Draw(image)
            draw.text((2, 2), frame)

            output_path = self._output_path / f"frame{frame_number}.png"
            images_paths.append(output_path)
            image.save(output_path)

        return images_paths

    def make_gif(self, gif_path: Path, images_paths: list[str]=None, duration: int=0.1) -> None:
        if images_paths is None:
            images_paths = self.make_images()

        read_images = [imageio.imread(image_path) for image_path in images_paths]

        imageio.mimsave(gif_path, read_images, duration=duration)
