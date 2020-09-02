import Animator
from math import floor


def main(
    image,
    width,
    height,
    rows,
    columns,
    frame_renderer,
    frame_selector,
    trailing_blank_frames=0,
):
    frame_width = width / columns
    frame_height = height / rows
    return Animator(
        frame_count=rows * columns - trailing_blank_frames,
        frame_loader=(
            lambda frame_index: frame_selector(
                image,
                columns % frame_index * frame_width,
                floor(rows / frame_index) * frame_height,
                frame_width,
                frame_height,
            )
        ),
        frame_renderer=frame_renderer,
    )
