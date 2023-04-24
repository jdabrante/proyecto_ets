from datetime import datetime


class Round:
    def __init__(self, hand: str):
        self.hand = hand
        self.outcome = "unknown"

    def update_outcome(self, outcome: str):
        self.outcome = outcome

    def generate_number(self, current_game):
        self.number = current_game.next_available_id

    def __str__(self):
        return f"Ronda nº: {self.number}\nMano: {self.hand}\nResultado: {self.outcome}"


class Game:
    def __init__(self, name: str):
        self.start_datetime = datetime.now()
        self.name = name
        self.rounds = []
        self.next_available_id = 0

    def calc_duration(self):
        self.duration = datetime.now() - self.start_datetime

    def add_round(self, round):
        round.generate_number(self)
        self.rounds.append(round)
        self.next_available_id += 1


class Map:
    pass


test_object = Game("hola")
test_round = Round("AA")
test_object.add_round(test_round)
print(test_object.rounds[0])
test_round = "hola"
print(test_object.rounds[0])
test_round1 = Round("AK")
test_object.add_round(test_round1)
print(test_object.rounds[1])
