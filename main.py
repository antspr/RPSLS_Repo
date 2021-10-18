from player import Player
from human import Human

human_1 = Human()
human_2 = Human()

human_1.choose_gesture()

gestures = ["rock", "paper", "scissors", "lizard", "spock"]

if human_1.choice == "rock":
    human_1.rock_logic()
