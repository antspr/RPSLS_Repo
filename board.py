from player import Player
from rules import Rules


class Board():
    def __init__(self):
        self.rules = Rules()
        self.welcome_message()
        self.human = True

    def welcome_message(self):
        print("Welcome to RPSLS!")

    def choose_opponent(self):
        opponent = input("""Which game mode would you like to play? 
        Choose "1" for single player
        Choose "2" multiplayer?
        """)
        if opponent == '1':
            self.human == False
        else:
            self.human == True

    def player_1_turn(self):
        self.player_1.choose_gesture()
        pass

    def player_2_turn(self):
        self.player_2.choose_gesture()
        pass

    def compare(self):
        # player_1.choose_gesture()
        pass
