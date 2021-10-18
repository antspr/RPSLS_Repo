class Rules:  # initialize on board
    def __init__(self):
        self.name = ""

    def tie(self):
        pass

    def rock_logic(self):
        if player_2.choice == "lizard" or "scissors":
            print(f"{player_1.choice} crushes {player_2.choice}! ")
        elif player_2.choice != "lizard" or "scissors":
            print(f"{player_1.choice} is crushed by {player_2.choice}! ")

    def paper_logic(self):
        pass

    def scissors_logic(self):
        pass

    def lizard_logic(self):
        pass

    def spock_logic(self):
        pass
