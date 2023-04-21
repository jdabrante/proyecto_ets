from datetime import datetime


class Round:
    pass


class Game:
    def __init__(self):
        self.date = datetime.now()

    pass


class Map:
    pass


test_object = Game()
print(test_object.date)
