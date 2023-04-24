from datetime import datetime
PATH = "odds"

class Round:
    def __init__(self, hand: str):
        self.hand = hand
        self.outcome = "unknown"

    def update_outcome(self, outcome: str):
        self.outcome = outcome

    def generate_number(self, current_game):
        self.number = current_game.next_available_round_id

    def __str__(self):
        return f"Ronda nº: {self.number}\nMano: {self.hand}\nResultado: {self.outcome}"


class Game:
    def __init__(self, name: str):
        self.start_datetime = datetime.now()
        self.name = name
        self.rounds = []
        self.next_available_round_id = 0
        self.hands_odds = self.init_hands_odds()

    def init_hands_odds(self):
        hands_odds = {}
        with open(PATH) as f:
            for line in f:
                clean_line = line.strip().split(":")
                user_hand, rival_hand, odds = clean_line
                hands_odds[user_hand][rival_hand] = odds
        return hands_odds

    def calc_duration(self):
        self.duration = datetime.now() - self.start_datetime

    def add_round(self, round):
        round.generate_number(self)
        self.rounds.append(round)
        self.next_available_round_id += 1


class Map:
    def __init__(self, round, game):
        self.odds = self.get_odds(round.hand, game)


    def get_odds(self,round, game):
        return game.hands_odds[round.hand]




test_object = Game("hola")
test_round = Round("AA")
test_object.add_round(test_round)
print(test_object.rounds[0])
test_round = "hola"
print(test_object.rounds[0])
test_round1 = Round("AK")
test_object.add_round(test_round1)
print(test_object.rounds[1])
