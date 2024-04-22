import tkinter as tk
import tkinter.messagebox
import random
class TicTacToe:
    def __init__(self, window):
        self.window = window
        self.window.title("Tic Tac Toe")
        self.player_symbol = "X"
        self.computer_symbol = "O"
        self.board = [" " for j in range(9)]
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(window, text=" ", font=("Arial", 20), width=5, height=2,command=lambda i=i, j=j: self.player_move(i, j))
                button.grid(row=i, column=j, sticky="nsew")
                row.append(button)
            self.buttons.append(row)
        self.status_label = tk.Label(window, text="Your turn (X)", font=("Arial", 14))
        self.status_label.grid(row=3, columnspan=3)
    def player_move(self, i, j):
        if self.board[i * 3 + j] == " ":
            self.update_board(i * 3 + j, self.player_symbol)
            if self.check_win(self.player_symbol):
                self.game_over("You win!")
            elif " " not in self.board:
                self.game_over("It's a draw!")
            else:
                self.computer_move()
    def computer_move(self):
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = self.computer_symbol
                if self.check_win(self.computer_symbol):
                    self.update_board(i, self.computer_symbol)
                    self.game_over("Computer wins!")
                    return
                self.board[i] = " "  
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = self.player_symbol
                if self.check_win(self.player_symbol):
                    self.board[i] = self.computer_symbol
                    self.update_board(i, self.computer_symbol)
                    return
                self.board[i] = " "  
        while True:
            index = random.randint(0, 8)
            if self.board[index] == " ":
                self.update_board(index, self.computer_symbol)
                break
        if self.check_win(self.computer_symbol):
            self.game_over("Computer wins!")
        elif " " not in self.board:
            self.game_over("It's a draw!")
        else:
            self.status_label.config(text="Your turn (X)")
    def update_board(self, index, symbol):
        self.buttons[index // 3][index % 3].config(text=symbol, state="disabled")
        self.board[index] = symbol
    def check_win(self, symbol):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for i, j, k in winning_combinations:
            if self.board[i] == self.board[j] == self.board[k] == symbol:
                return True
    def game_over(self, message):
        result = tkinter.messagebox.askquestion("Game Over", f"{message} Do you want to play again?")
        if result == "yes":
            self.reset_game()
        else:
            self.window.quit()
            self.window.destroy()

def main():
    window = tk.Tk()
    game = TicTacToe(window)
    window.mainloop()
if __name__ == "__main__":
    main()
