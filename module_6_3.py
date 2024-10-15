class Horse:
    x_distance = 0
    sound = 'Frrr'

    def __init__(self, x_distance, sound):
        self.x_distance = x_distance
        self.sound = sound
        super().__init__()

    def run(self, dx):
        dx += self.x_distance

class Eagle:

    y_distance = 0
    sound = 'I train, eat, sleep and repeat'

    def __init__(self, y_distance, sound):
        self.y_distance = y_distance
        self.sound = sound
        super().__init__()

    def fly(self, dy):
        dy += self.y_distance

class Pegasus (Horse, Eagle):

    def __init__(self, x_distance, y_distance, sound):
        super().__init__(x_distance)
        super().__init__(y_distance, sound)

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return super().x_distance, super().y_distance

    def voice(self):
        return super().sound

p1 = Pegasus(0,0,'I train, eat and sleep')

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5,20)
print(p1.get_pos())

p1.voice()
