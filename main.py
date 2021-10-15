what_would_happen = []


class Player():
    def __init__(self):
        self.choose_gesture()

    def choose_gesture(self):
        print("test")
        pass


class Human(Player):
    def __init__(self):
        super().__init__(self)

    # def choose_gesture(self):
    #     return super().choose_gesture()
    human_1 = Player().Human()
    human_1.choose_gesture()

    gestures = [rock, paper, scissors, lizard, spock]
    human_1.choose_gesture = input("Which option would you like ot pick?")

    counter = 0
    for option in gestures:
