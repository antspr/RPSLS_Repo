from ai import Ai
from player import Player
from rules import Rules
from human import Human



class Board():
    def __init__(self):
        self.rules = Rules()
        player_1 = Human()
        player_2 = None

    def rungame(self):
        self.welcome_message()
        self.rules_list
        self.choose_opponent()

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
                player_2 = Ai()
                opponent_chosen = True
            elif opponent == "2":
                player_2 = Human()
                opponent_chosen = True
            else:
                print("Wrong input")

    def play_game(self):
        round_count = 0
        self.player_1_turn()
        self.player_2_turn()
        self.compare
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

        pass

board_1 = Board()
player_1 = Player()
player_2 = Player()
board_1.choose_opponent()
player_1.choose_name()

player_1.player_1_turn()


gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]


if player_1.choice == "Rock":
    board_1.rules.rock_logic()
    print('user chose rock')




    def tie(self):
        pass

    def rock_logic(self):
        if self.player_2.choice == "lizard" or "scissors":
            print(f"{player_1.choice} crushes {player_2.choice}! ")
        elif self.player_2.choice != "lizard" or "scissors":
            print(f"{player_1.choice} is crushed by {player_2.choice}! ")

    def paper_logic(self):
        pass

    def scissors_logic(self):
        pass

    def lizard_logic(self):
        pass

    def spock_logic(self):