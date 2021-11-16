import math
import random


class TicTacToeBoard:
    """The Tic-Tac-Toe Board"""
    def __init__(self, player1="Player 1", player2="Player 2", size=3, symbol1='O', symbol2='X', random_start=True):
        self.__size = size
        self.__board = []
        for i in range(self.__size):
            self.__board.append([None] * self.__size)
        self.__symbol1 = symbol1.strip()
        self.__symbol2 = symbol2.strip()
        self.__player1 = player1.strip()
        self.__player2 = player2.strip()
        if random_start:
            self.__next_move = random.choice([self.__symbol1, self.__symbol2])
        self.__current_move_count = 0

    def show_board(self):
        space_between_top_label = 5

        for i in range(self.__size):
            print(" " * space_between_top_label, i+1, end="")
        print()
        print("  |" + "-" * space_between_top_label * (self.__size + 1), end="|\n")

        for i in range(self.__size):
            print(i+1, "|", end="")
            for j in range(self.__size):
                if self.__board[i][j] is not None:
                    print(" " * math.ceil(space_between_top_label/2), self.__board[i][j], " " * math.floor(space_between_top_label/2), "|", sep="", end="")
                else:
                    print(" " * space_between_top_label, " |", sep="", end="")
            print()
            print("  |" + "-" * space_between_top_label * (self.__size+1), end="|\n")

    def make_move(self, location_x, location_y):
        if self.check_valid_move(location_x, location_y):
            self.__board[location_x-1][location_y-1] = self.__next_move
            self.__next_move = self.__symbol1 if self.__next_move == self.__symbol2 else self.__symbol2
            self.__current_move_count += 1
        else:
            print("Invalid move!")

    def check_valid_move(self, location_x, location_y):
        if location_x <= 0 or location_x > self.__size or location_y <= 0 or location_y > self.__size:
            return False
        elif self.__current_move_count >= self.__size * self.__size or self.__board[location_x-1][location_y-1] is not None:
            return False
        return True

    def check_win_condition(self):
        winning_symbol = None
        diagonal1 = []
        diagonal2 = []
        for i in range(self.__size):
            if len(set(self.__board[i])) == 1 and None not in set(self.__board[i]):
                winning_symbol = self.__board[i][0]
                break

            column = []
            for j in range(self.__size):
                column.append(self.__board[j][i])
            if len(set(column)) == 1 and None not in set(column):
                winning_symbol = self.__board[0][i]
                break

            diagonal1.append(self.__board[i][i])
            diagonal2.append(self.__board[self.__size-1-i][i])

        if len(set(diagonal1)) == 1 and None not in set(diagonal1):
            winning_symbol = self.__board[0][0]

        if len(set(diagonal2)) == 1 and None not in set(diagonal2):
            winning_symbol = self.__board[self.__size-1][0]

        if winning_symbol is not None:
            return self.get_winning_player(winning_symbol)
        else:
            return False

    def get_winning_player(self, winning_symbol):
        return self.__player1 if winning_symbol == self.__symbol1 else self.__player2

    def get_next_move(self):
        return self.__next_move

    def play(self):
        print(self.__player1 if self.__next_move == self.__symbol1 else self.__player2, "will start the game!")
        exit_condition = False
        while not exit_condition:
            self.show_board()
            while True:
                try:
                    print("Enter exit to exit game early!")
                    move = input("Enter your move as an x and y coordinate separated by a comma (x,y): ")
                    if move.strip().lower() == "exit":
                        exit_condition = True
                        break
                    move_list = move.split(",")
                    if len(move_list) < 2:
                        raise Exception
                    self.make_move(int(move_list[0].strip()), int(move_list[1].strip()))
                except:
                    print("Invalid input!")
                else:
                    break
            if exit_condition:
                break
            else:
                exit_condition = self.check_win_condition()
