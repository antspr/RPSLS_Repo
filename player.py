class Player:
    def __init__(self):
        self.win_counter = 0
        self.choice = ""

    def choose_name(self):
        self.name = input("Insert name: ")

    def choose_gesture(self):  # how to return value to be manipulated
        validation = False
        while validation == False:
            self.choice = input(f"""{self.name}, which option would you like to pick?
            1 for rock,
            2 is paper, 
            3 is scissor, 
            4 is lizard,
            5 is spock
            """)
            if self.choice == "1":
                self.choice = "Rock"
                validation = True
                return self.choice
            elif self.choice == "2":
                self.choice = "Paper"
                validation = True
                return self.choice
            elif self.choice == "3":
                self.choice = "Scissors"
                validation = True
                return self.choice
            elif self.choice == "4":
                self.choice = "Lizard"
                validation = True
                return self.choice
            elif self.choice == "5":
                self.choice = "Spock"
                validation = True
                return self.choice
            else:
                print("Invalid choice, try again.")
                continue
