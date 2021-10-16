class Player:
    def __init__(self, name):
        self.name = name

    def choose_gesture(self):  # how to return value to be manipulated
        self.choice = int(input("""Which option would you like to pick?
        1 for rock,
        2 is paper, 
        3 is scissor, 
        4 is lizard,
        5 is spock
        """))
