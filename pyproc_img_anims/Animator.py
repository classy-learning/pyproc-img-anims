class Animator:
    def __init__(self, frame_count, frame_loader, frame_renderer):
        self.__frame_count = frame_count
        self.__frame_loader = frame_loader
        self.__frame_renderer = frame_renderer
        self.reversed = False

    def __render(self, x, y):
        frame = self.__frame_loader(self.__frame_index)
        self.__frame_renderer(frame, x, y)

    def __step(self):
        self.__frame_index += -1 if self.reversed else 1
        if self.__frame_index < 0:
            self.__frame_index = self.__frame_count - 1
        elif self.__frame_index >= self.__frame_count:
            self.__frame_index = 0

    def draw(self, x, y):
        __render(self, x, y)
        __step()

    def setup(self):
        self.__frame_index = self.__frame_count if self.reversed else 0
