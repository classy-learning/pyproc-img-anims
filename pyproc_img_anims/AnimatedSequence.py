import Animator


def main(images, frame_renderer):
    return Animator(
        frame_count=len(images),
        frame_loader=lambda frame_index: images[frame_index],
        frame_renderer=frame_renderer,
    )
