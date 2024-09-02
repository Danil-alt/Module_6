class Horse:

    x_distance = 0
    sound = 'Frrr'
    def run(self, dx):
        self.x_distance += dx

class Eagle:

    y_distance = 0
    _sound = 'I train, eat, sleep, and repeat'
    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):

    def __init__(self):
        self.sound = super().sound
        self.sound = super()._sound

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        pos_pegasus = (self.x_distance, self.y_distance)
        return pos_pegasus

    def voice(self):
        print(self.sound)

pegas = Pegasus()
print(pegas.get_pos())
pegas.move(5, -7)
print(pegas.get_pos())
pegas.move(-6, 10)
print(pegas.get_pos())
pegas.voice()
print(Pegasus.mro())