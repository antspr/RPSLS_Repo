from random import randint
import random

from player import Player

gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

class Ai(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        self.choice = random.choice(gestures)
        return self.choice

           
            
