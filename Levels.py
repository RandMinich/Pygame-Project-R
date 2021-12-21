import Load_image


class Level:
    def __init__(self, gravity, background_image):
        self.bgi = Load_image.load_image(background_image)
        self.gravity = gravity
        self.objects = []
        self.running

    def append_object(self, object):
        self.objects.append(object)

    def play(self, First_Screen):
        First_Screen.draw(self.bgi)

    def run_level(self, screen, is_running_flag):
        while sel.running:
           ...
