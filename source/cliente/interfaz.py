from datetime import datetime


class Round:
    def __init__(self, id: int):
        self.id = id

class Game:
    def __init__(self, name: str):
        self.start_datetime = datetime.now()
        self.name = name
        self.rounds = []

    def calc_duration(self):
        self.duration = datetime.now() - self.date

    def add_round(self, round):
        self.rounds.append(round)

class Map:
    pass


test_object = Game('hola')
test_round = Round(1)
test_object.add_round(test_round)
print(test_object.rounds)
