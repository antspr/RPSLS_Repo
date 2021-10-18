from player import Player
from board import Board

board_1 = Board()
player_1 = Player()
player_2 = Player()
board_1.choose_opponent()
player_1.choose_name()

player_1.player_1_turn()


gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

if player_1.choice == "Rock":
    board_1.rules.rock_logic()
    print('user chose rock')
