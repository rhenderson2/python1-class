# homework assignment section 9-13
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        from random import randint
        print(randint(1, self.sides))

side6 = Die()
side6.roll_die()
my_die10 = Die(10)
my_die10.roll_die()
my_die20 = Die(20)
my_die20.roll_die()
