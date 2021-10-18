from ai import Ai
from player import Player
from rules import Rules
from human import Human


class Board():
    def __init__(self):
        self.rules = Rules()
        self.welcome_message()
        self.human = True
        player_1 = Human()
        player_2 = None

    def welcome_message(self):
        print("Welcome to RPSLS!")

    def choose_opponent(self):
        opponent_chosen = False
        while opponent_chosen == False:
            opponent = input("""Which game mode would you like to play? 
            Choose "1" for single player
            Choose "2" multiplayer?
            """)
            if opponent == '1':
                player_2 = Ai()
                opponent_chosen = True
            elif opponent == "2":
                player_2 = Human()
                opponent_chosen = True
            else:
                print("Wrong input")

    def player_1_turn(self):
        self.player_1.choose_gesture()
        pass

    def player_2_turn(self):
        self.player_2.choose_gesture()
        pass

    def compare(self):
        # player_1.choose_gesture()
        pass
