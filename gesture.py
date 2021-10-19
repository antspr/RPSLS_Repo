

class Gesture():
    def __init__(self): 
        self.list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    
    def rock_logic(self):
        if self.player_1.choice == self.player_2.choice:
            print("Tie! ")
        elif self.player_2.choice == "Lizard" or self.player_2.choice == "Scissors":
            print(f"{self.player_1.choice} crushes {self.player_2.choice}! ")
            self.player_1.win_counter += 1
        else:
            print(f"{self.player_1.choice} is beaten by {self.player_2.choice}! ")
            self.player_2.win_counter += 1

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