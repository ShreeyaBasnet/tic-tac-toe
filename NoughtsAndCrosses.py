import random
import os.path
import json

random.seed()


def draw_board(board):
    """Shows the game grid"""
    print("\n 1 2 3")
    print(" -------------")
    for i in range(3):
        print(f"{i+1} | {board[i][0]} | {board[i][1]} | {board[i][2]} |")
        print(" -------------")

def welcome(board):
    """Prints welcome message and grid"""
    print("Welcome to the Unbeatable Noughts and Crosses Game!")
    draw_board(board)

def initialise_board(board):
    """Clears the grid"""
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
    return board

def get_player_move(board):
    """Gets player's move"""
    while True:
        try:
            row = int(input("Enter the row (1-3) for your move: ")) - 1
            col = int(input("Enter the column (1-3) for your move: ")) - 1
            if 0 <= row < 3 and 0 <= col < 3:
                if board[row][col] == ' ':
                    return row, col
                else:
                    print("Cell already taken. Try again.")
            else:
                print("Invalid input. Please enter values from 1 to 3.")
        except ValueError:
            print("Invalid input. Please enter numbers.")

def choose_computer_move(board):
    """Picks computer's move"""
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(available_moves)

def check_for_win(board, mark):
    """Checks for a win"""
    for i in range(3):
        if all(board[i][j] == mark for j in range(3)):
            return True
        if all(board[j][i] == mark for j in range(3)):
            return True
    if all(board[i][i] == mark for i in range(3)):
        return True
    if all(board[i][2 - i] == mark for i in range(3)):
        return True
    return False

def check_for_draw(board):
    """Checks for a draw"""
    for row in board:
        if ' ' in row:
            return False
    return True


def play_game(board):
    """Runs a game"""
    initialise_board(board)
    draw_board(board)
    while True:
        row, col = get_player_move(board)
        board[row][col] = 'X'
        draw_board(board)
        if check_for_win(board, 'X'):
            print("You win!")
            return 1
        if check_for_draw(board):
            print("It's a draw!")
            return 0
        print("Computer's move:")
        row, col = choose_computer_move(board)
        board[row][col] = 'O'
        draw_board(board)
        if check_for_win(board, 'O'):
            print("Computer wins!")
            return -1
        if check_for_draw(board):
            print("It's a draw!")
            return 
def menu():
    """Shows menu and gets choice"""
    print("\nMenu:")
    print("1 - Play the game")
    print("2 - Save score")
    print("3 - Load and display scores")
    print("q - Quit")
    while True:
        choice = input("Enter your choice: ").lower()
        if choice in ['1', '2', '3', 'q']:
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, 3, or q.")

def load_scores():
    """Loads leaderboard scores"""
    leaders = {}
    if os.path.isfile('leaderboard.txt'):
        with open('leaderboard.txt', 'r') as file:
            try:
                leaders = json.load(file)
            except json.JSONDecodeError:
                leaders = {}
    return leaders

def save_score(score):
    """Saves player's score"""
    name = input("Enter your name: ")
    leaders = load_scores()
    if name in leaders:
        leaders[name] += score
    else:
        leaders[name] = score
    with open('leaderboard.txt', 'w') as file:
        json.dump(leaders, file)

def display_leaderboard(leaders):
    """Shows sorted leaderboard"""
    if not leaders:
        print("Leaderboard is empty.")
    else:
        print("\nLeaderboard:")
        for name, score in sorted(leaders.items(), key=lambda x: x[1], reverse=True):
            print(f"{name}: {score}")

