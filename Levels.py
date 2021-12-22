import Load_image


class Level:
    def __init__(self, gravity, background_image):
        self.bgi = Load_image.load_image(background_image)
        self.gravity = gravity
        self.groups = []

    def append_object(self, group):
        self.groups.append(group)

    def play(self, First_Screen):
        running = True
        while running:
            First_Screen.fill(0, 0, 0)
            First_Screen.draw(self.bgi)
            First_Screen.flip()
