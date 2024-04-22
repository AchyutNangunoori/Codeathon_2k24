import tkinter as tk
import tkinter.messagebox
import random
class TicTacToe:
    def __init__(self, window):
        self.window = window
        self.window.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [" " for j in range(9)]
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(window, text=" ", font=("Arial", 40), width=5, height=2,command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j, sticky="nsew")
                row.append(button)
            self.buttons.append(row)
        self.status_label = tk.Label(window, text="Player X's turn", font=("Arial", 14))
        self.status_label.grid(row=3, columnspan=3)
    def make_move(self, i, j):
        if self.board[i * 3 + j] == " ":
            self.buttons[i][j].config(text=self.current_player, state="disabled")
            self.board[i * 3 + j] = self.current_player
            if self.check_win():
                self.game_over()
            elif " " not in self.board:
                self.game_over(draw=True)
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s turn")
    def check_win(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for i, j, k in winning_combinations:
            if self.board[i] == self.board[j] == self.board[k] != " ":
                return True
        return False
    def game_over(self, draw=False):
        if draw:
            result = tkinter.messagebox.askquestion("Game Over", "It's a draw! Do you want to play again?")
        else:
            winner = "Player O" if self.current_player == "O" else "Player X"
            result = tkinter.messagebox.askquestion("Game Over", f"{winner} wins! Do you want to play again?")

        if result == "yes":
            self.reset_game()
        else:
            self.window.quit()
            self.window.destroy()

    def reset_game(self):
        self.window.destroy()
        main()

def main():
    window = tk.Tk()
    game = TicTacToe(window)
    window.mainloop()
if __name__ == "__main__":
    main()
