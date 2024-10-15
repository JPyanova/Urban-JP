class Horse:

    def __init__(self, x_distance, sound):
        self.x_distance = 0
        self.sound = 'Frrr'
        super().__init__()

    def run(self, dx):
        dx = self.x_distance + dx

class Eagle:

    def __init__(self, y_distance, sound):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep and repeat'
        super().__init__()

    def fly(self, dy):
        dy = self.y_distance + dy

class Pegasus (Horse, Eagle):

    def __init__(self, x_distance, y_distance, sound):
        super().__init__(x_distance)
        super().__init__(y_distance, sound)

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        position = [self.x_distance, self.y_distance]

    def voice(self):
        inherited_voice = self.voice

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
