
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
        while self.player_1.win_counter < 2 and self.player_2.win_counter < 2:
            self.player_1_turn()
            self.player_2_turn()
            self.compare()
            self.check_winner()

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

    def check_winner(self):
        if self.player_1.win_counter >= 2:
            print(f"Congratulations {self.player_1.name} you have won! ")
        elif self.player_2.win_counter >= 2:
            print(f"Congratulations {self.player_2.name} you have won! ")

    def rock_logic(self):
<<<<<<< HEAD
         if self.player_2.choice == "Lizard" or "Scissors":
             print(f"{self.player_1.choice} crushes {self.player_2.choice}! ")
         else:
             print(f"{self.player_1.choice} is crushed by {self.player_2.choice}! ")
=======
        if self.player_1.choice == self.player_2.choice:
            print("Tie! ")
        elif self.player_2.choice == "Lizard" or self.player_2.choice == "Scissors":
            print(f"{self.player_1.choice} crushes {self.player_2.choice}! ")
            self.player_1.win_counter += 1
        else:
            print(f"{self.player_1.choice} is beaten by {self.player_2.choice}! ")
            self.player_2.win_counter += 1
>>>>>>> c15032d907302b7a0591503a426fa969fc3b799f

    def paper_logic(self):
        if self.player_1.choice == self.player_2.choice:
            print("Tie! ")
        elif self.player_2.choice == "Spock" or self.player_2.choice == "Rock":
            print(f"{self.player_1.choice} crushes {self.player_2.choice}! ")
            self.player_1.win_counter += 1
        else:
            print(f"{self.player_1.choice} is beaten by {self.player_2.choice}! ")
            self.player_2.win_counter += 1

    def scissors_logic(self):
        if self.player_1.choice == self.player_2.choice:
            print("Tie! ")
        elif self.player_2.choice == "Paper" or self.player_2.choice == "Lizard":
            print(f"{self.player_1.choice} crushes {self.player_2.choice}! ")
            self.player_1.win_counter += 1
        else:
            print(f"{self.player_1.choice} is beaten by {self.player_2.choice}! ")
            self.player_2.win_counter += 1

    def lizard_logic(self):
        if self.player_1.choice == self.player_2.choice:
            print("Tie! ")
        elif self.player_2.choice == "Spock" or self.player_2.choice == "Paper":
            print(f"{self.player_1.choice} crushes {self.player_2.choice}! ")
            self.player_1.win_counter += 1
        else:
            print(f"{self.player_1.choice} is beaten by {self.player_2.choice}! ")
            self.player_2.win_counter += 1

    def spock_logic(self):
        if self.player_1.choice == self.player_2.choice:
            print("Tie! ")
        elif self.player_2.choice == "Scissors" or self.player_2.choice == "Rock":
            print(f"{self.player_1.choice} crushes {self.player_2.choice}! ")
            self.player_1.win_counter += 1
        else:
            print(f"{self.player_1.choice} is beaten by {self.player_2.choice}! ")
            self.player_2.win_counter += 1
