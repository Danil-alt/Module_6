class Animal:
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        elif food.edible:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Plant:
    edible = False
    def __init__(self, name):
        self.name = name
    '''
    alive - живой
    fed - накормленность
    ebidle - съедобный
    '''
class Mammal(Animal):
    pass

class Predator(Animal):
   pass


class Flower(Plant):
    edible = True

class Fruit(Plant):
    edible = True

q1 = Predator('Lion')
q2 = Mammal('Horse')
q3 = Fruit('Apple')
q4 = Flower('Clover')

print(q1.name)
print(q3.name)
print(q4.edible)
print(q2.fed)
q2.eat(q3)
print(q2.fed)
