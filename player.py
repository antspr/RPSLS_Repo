class Player:
    def __init__(self, name):
        self.name = name
        self.human = True

    def choose_opponent(self):
        opponent = input("""Which game mode would you like to play? 
        Choose "1" for single player
        Choose "2" multiplayer?""")
        if opponent == '1':
             self.human == False
             
        else:
            self.human == True
    
    def choose_gesture(self):  # how to return value to be manipulated
        self.choice = input("""Which option would you like to pick?
        1 for rock,
        2 is paper, 
        3 is scissor, 
        4 is lizard,
        5 is spock
        """)
        if self.choice == '1':
            self.choice = 'Rock'
        elif self.choice == '2':
            self.choice = 'Paper'
        elif self.choice == '3':
            self.choice = 'Scissors'
        elif self.choice == '4':
            self.choice = 'Lizard'
        elif self.choice == '5':
            self.choice = 'Spock'
        return self.choice