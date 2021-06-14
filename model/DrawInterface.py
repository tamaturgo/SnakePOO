class DrawInterface:
    def __init__(self):
        self.y = None
        self.x = None
        self.image = None
        self.parent_screen = None
        self.length = None

    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))

    def draw_apple(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
