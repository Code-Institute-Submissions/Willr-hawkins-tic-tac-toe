### Imports for libaries
import random
from art import *
import colorama
from colorama import Fore, Style

### Automatically reset the color.
colorama.init(autoreset=True)

### Global variables:
board_numbers = [1,2,3,4,5,6,7,8,9]
board = [[1,2,3], [4,5,6], [7,8,9]]
rows = 3
cols = 3



def new_game():
    """
    Introduce the player to the game, ask for player name input.
    """
    Art = text2art('Tic Tac Toe')
    print(Art)
    print('_' * 35)
    print('This is a single player game against a computer.')
    print('_' * 35)
    player_name = input('Please enter your name:\n')


def game_board():
    """
    Creates a board for the game.
    """

    for x in range(rows):
        print('\n+---+---+---+')
        print('|', end = '')
        for y in range(cols):
            print('', board[x][y], end = ' |')
    print('\n+---+---+---+')


def update_board(num, turn):
    """
    Updates the numbers on the game board.
    checks whether the player or computer picked 
    the number.
    """
    num -= 1

    if(num == 0):
        board[0][0] = turn
    elif(num == 1):
        board[0][1] = turn
    elif(num == 2):
        board[0][2] = turn
    elif(num == 3):
        board[1][0] = turn
    elif(num == 4):
        board[1][1] = turn
    elif(num == 5):
        board[1][2] = turn
    elif(num == 6):
        board[2][0] = turn
    elif(num == 7):
        board[2][1] = turn
    elif( num == 8):
        board[2][2] = turn


def get_board_values():
    """
    Gets the value for the number on the board,
    Whether it is 'X' (players turn) or 'O' (computers turn).
    """

    end_game = False
    player_turn = (Fore.GREEN + 'X')
    computer_turn = (Fore.CYAN + 'O')
    turn_number = 0

    while(end_game == False):
        if (turn_number % 2 == 1):
            game_board()
            player_choice = int(input('\nPlease choose a number between 1 - 9:\n'))
            print('_' * 35)
            if (player_choice >= 1 or player_choice <= 9):
                update_board(player_choice, player_turn)
                board_numbers.remove(player_choice) 
            else:
                print('Invalid number, please pick again.')
            turn_number += 1
        else:
            while(True):
                computer_choice = random.choice(board_numbers)
                print(f'{computer_choice} was picked by the computer.\n')
                print('_' * 35)
                if(computer_choice in board_numbers):
                    update_board(computer_choice, computer_turn)
                    board_numbers.remove(computer_choice)
                    turn_number += 1
                    break


def check_winner():
    """
    Checks all ways either the player or computer could win.
    And whether it is the player or computer that wins, or if
    there is no winner.
    """

def main():
    """
    Runs all the games functions.
    """
    new_game()
    game_board()
    get_board_values()
    
    
main()

