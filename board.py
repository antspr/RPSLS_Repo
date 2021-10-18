from types import NoneType
from ai import Ai
from player import Player
from human import Human

gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

class Board():
    def __init__(self):
        self.player_1 = Human()
        self.player_2 = None

    def rungame(self):
        self.welcome_message()
        self.rules_list()
        self.choose_opponent()
        self.play_game()

    def welcome_message(self):
        print("Welcome to RPSLS!")

    def rules_list(self):
        print("""The rules of the game are as follows
        Best best of 3 rounds wins
        winners 
        Rock > Scissor and Lizard
        Spock > Scissor and Rock
        Paper > Spock and Rock
        Scissor > Paper and Lizard
        Lizard > Spock and Paper""")


    
    def choose_opponent(self):
        opponent_chosen = False
        while opponent_chosen == False:
            opponent = input("""Which game mode would you like to play? 
            Choose "1" for single player
            Choose "2" multiplayer?
            """)
            if opponent == '1':
                self.player_2 = Ai()
                opponent_chosen = True
            elif opponent == "2":
                self.player_2 = Human()
                opponent_chosen = True
            else:
                print("Wrong input")

    def play_game(self):
        round_count = 0
        self.player_1_turn()
        self.player_2_turn()
        self.compare()
    def player_1_turn(self):
        self.player_1.choose_gesture()
        return

    def player_2_turn(self):
        self.player_2.choose_gesture()
        pass

    def compare(self):
        if self.player_1.choice == 'Rock':
            self.rock_logic()
        elif self.player_1.choice == "Paper":
            self.paper_logic()
        elif self.player_1.choice == "Scissors":
            self.scissors_logic()
        elif self.player_1.choice == "Lizard":
            self.lizard_logic()
        elif self.player_1.choice == "Spock":
            self.spock_logic()
            pass

    def rock_logic(self):
         if self.player_2.choice == "lizard" or "scissors":
             print(f"{self.player_1.choice} crushes {self.player_2.choice}! ")
         else:
             print(f"{self.player_1.choice} is crushed by {self.player_2.choice}! ")

    def paper_logic(self):
         pass

    def scissors_logic(self):
         pass

    def lizard_logic(self):
         pass

    def spock_logic(self):
         pass