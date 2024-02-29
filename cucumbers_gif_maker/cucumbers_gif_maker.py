from pathlib import Path


class CucumbersGifMaker:
    def __init__(self, frames: list[str]):
        self._frames = frames

    def save_gif(self, git_path: Path) -> None:
        pass