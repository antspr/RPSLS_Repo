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
    human_1.choose_gesture = int(input(f'"""Which option would you like ot pick?1 for rock,
    2 is paper, 
    3 is scissor, 
    lizard is 4,
    spock is 5 """'))
    choice = human_1.choosegesture
    counter = 0
<<<<<<< HEAD
    for option in gestures:


if user_1_choice == "rock" and user_2_choice == "lizard" or "scissors":
    print(f"{user_1_choice} crushes {user_2_choice}!")
elif user_1_choice == "rock" and user_2_choice != "lizard" or "scissors":
    print(f"{user_1_choice} is crushed by {user_2_choice}!")
=======

    for option in range(len(gestures)-1):
    
            gesture[0]   gestures[2]
        #print(f'{i} - {option})
        if human_1.choose_gesture == 0
        counter += 1

if user_1_choice == "rock" and user_2_choice =="lizard" or "scissors":
    print (f"{user_1_choice} crushes {user_2_choice}" !)
elif user_1_choice == "rock" and user_2_choice !="lizard" or "scissors":
    print (f"{user_1_choice} is crushed by {user_2_choice}! ")
>>>>>>> 6328d9f57b1c49abc4ae679232c47e109179b715
