import tkinter as tk
import tkinter.messagebox
import random
class ModeSelectionPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Game Hub - Mode Selection")
        self.master.geometry("400x300")
        self.master.configure(bg='light blue')
        self.create_widgets()
    def create_widgets(self):
        button_bg = "#4a7a8c"
        button_fg = "white"
        button_font = ("Helvetica", 12, "bold")
        label = tk.Label(self.master, text="Game Hub", font=("Helvetica", 18, "bold"), bg='light blue')
        label.pack(pady=10)
        tic_tac_toe_2p_button = tk.Button(self.master, text="Tic Tac Toe (2 Players)", command=self.play_tic_tac_toe_2p, width=20, height=2, bg=button_bg, fg=button_fg, font=button_font)
        tic_tac_toe_2p_button.pack(pady=5)
        tic_tac_toe_vs_comp_button = tk.Button(self.master, text="Tic Tac Toe (vs Computer)", command=self.play_tic_tac_toe_vs_comp, width=20, height=2, bg=button_bg, fg=button_fg, font=button_font)
        tic_tac_toe_vs_comp_button.pack(pady=5)
        hangman_button = tk.Button(self.master, text="Hangman", command=self.play_hangman, width=20, height=2, bg=button_bg, fg=button_fg, font=button_font)
        hangman_button.pack(pady=5)
        game_2048_button = tk.Button(self.master, text="2048", command=self.play_game_2048, width=20, height=2, bg=button_bg, fg=button_fg, font=button_font)
        game_2048_button.pack(pady=5)
    def play_tic_tac_toe_2p(self):
        self.master.destroy()
        root = tk.Tk()
        tic_tac_toe_game = TicTacToe(root)
        root.mainloop()
    def play_tic_tac_toe_vs_comp(self):
        self.master.destroy()
        root = tk.Tk()
        tic_tac_toe_game_vs_comp = TicTacToeVsComputer(root)
        root.mainloop()
    def play_hangman(self):
        self.master.destroy()
        root = tk.Tk()
        mode_selection = msp1(root)
        root.mainloop()
    def play_game_2048(self):
        self.master.destroy()
        root = tk.Tk()
        root.title("2048 Game")
        def start_game(board_size):
            for widget in root.winfo_children():
                widget.destroy()
            game = Game2048GUI(root, board_size)
        btn_beginner = tk.Button(root, text="Beginner (4x4)", command=lambda: start_game(4))
        btn_standard = tk.Button(root, text="Standard (5x5)", command=lambda: start_game(5))
        btn_advanced = tk.Button(root, text="Advanced (6x6)", command=lambda: start_game(6))
        btn_beginner.pack(pady=5)
        btn_standard.pack(pady=5)
        btn_advanced.pack(pady=5)
        root.mainloop()
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
            self.window.destroy()
            root = tk.Tk()
            tic_tac_toe_game = TicTacToe(root)
            root.mainloop()
        else:
            self.reset_game()
    def reset_game(self):
        self.window.destroy()
        root = tk.Tk()
        mode_selection = ModeSelectionPage(root)
        root.mainloop()
class TicTacToeVsComputer:
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
            self.window.destroy()
            root = tk.Tk()
            tic_tac_toe_game_vs_comp = TicTacToeVsComputer(root)
            root.mainloop()
        else:
            self.reset_game()
    def reset_game(self):
        self.window.destroy()
        root = tk.Tk()
        mode_selection = ModeSelectionPage(root)
        root.mainloop()
class msp1:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game - Mode Selection")
        self.master.geometry("400x200")
        self.master.configure(bg='light blue')
        self.create_widgets()
    def create_widgets(self):
        button_bg = "#4a7a8c"
        button_fg = "white"
        button_font = ("Helvetica", 12, "bold")
        label = tk.Label(self.master, text="HANGMAN GAME", font=("Helvetica", 18, "bold"), bg='light blue')
        label.pack(pady=10)
        classic_mode_button = tk.Button(self.master, text="Classic Mode", command=lambda: self.select_mode("classic"), width=20, height=2, bg=button_bg, fg=button_fg, font=button_font)
        classic_mode_button.pack(pady=5)
        race_mode_button = tk.Button(self.master, text="Race Mode", command=lambda: self.select_mode("race"), width=20, height=2, bg=button_bg, fg=button_fg, font=button_font)
        race_mode_button.pack(pady=5)  
    def select_mode(self, mode):
        self.master.destroy()
        root = tk.Tk()
        game = HangmanGame(root, mode=mode)
        root.mainloop()
class HangmanGame:
    def __init__(self, master, mode):
        self.master = master
        self.master.title("Hangman Game")
        self.master.geometry("1000x750")
        self.master.configure(bg='light blue')
        self.mode = mode
        self.clue="Clue: It's a Programming Language"
        self.secret_word = self.choose_secret_word()
        self.correct_guesses = set()
        self.incorrect_guesses = set()
        self.attempts_left = 7 if mode == "classic" else None
        self.time_limit = 10 if mode == "race" else None
        self.initialize_gui()
        if self.mode == "race":
            self.start_timer()
    def initialize_gui(self):
        button_bg = "#4a7a8c"
        button_fg = "white"
        button_font = ("Helvetica", 12, "bold")
        self.clue_label = tk.Label(self.master, text=self.clue, font=("Helvetica", 14), bg='light blue')
        self.clue_label.pack(pady=5)
        self.hangman_canvas = tk.Canvas(self.master, width=300, height=300, bg="white")
        self.hangman_canvas.pack(pady=20)
        self.word_display = tk.Label(self.master, text="_ " * len(self.secret_word), font=("Helvetica", 30), bg='light blue')
        self.word_display.pack(pady=(20, 20))
        self.attempts_label = tk.Label(self.master, text=f"Attempts left: {self.attempts_left}", font=("Helvetica", 14), bg='light blue')
        self.attempts_label.pack(pady=(0, 10))
        self.timer_label = tk.Label(self.master, text="", font=("Helvetica", 14), bg='light blue')
        self.timer_label.pack(pady=(0, 10))
        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.pack(pady=5)
        self.setup_alphabet_buttons()
        self.reset_button = tk.Button(self.master, text="Reset Game", command=self.reset_game, width=20, height=2, bg=button_bg, fg=button_fg, font=button_font)
        self.reset_button.pack(pady=(10, 0))
    def setup_alphabet_buttons(self):
        button_bg = "#4a7a8c"
        button_fg = "white"
        button_font = ("Helvetica", 12, "bold")
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        upper_row = alphabet[:13]
        lower_row = alphabet[13:]
        upper_frame = tk.Frame(self.buttons_frame)
        upper_frame.pack()
        lower_frame = tk.Frame(self.buttons_frame)
        lower_frame.pack()
        for letter in upper_row:
            button = tk.Button(upper_frame, text=letter, command=lambda l=letter: self.guess_letter(l), width=4, height=2, bg=button_bg, fg=button_fg, font=button_font)
            button.pack(side="left", padx=2, pady=2)
        for letter in lower_row:
            button = tk.Button(lower_frame, text=letter, command=lambda l=letter: self.guess_letter(l), width=4, height=2, bg=button_bg, fg=button_fg, font=button_font)
            button.pack(side="left", padx=2, pady=2)
    def choose_secret_word(self):
        with open("programming_languages.txt", "r") as file:
            words = [word.strip().upper() for word in file]
        return random.choice(words)
    def update_hangman_canvas(self):
        self.hangman_canvas.delete("all")
        stages = [self.draw_head, self.draw_body, self.draw_left_arm, self.draw_right_arm,self.draw_left_leg, self.draw_right_leg, self.draw_face]
        for i in range(len(self.incorrect_guesses)):
            if i < len(stages):
                stages[i]()
    def draw_head(self):
        self.hangman_canvas.create_oval(125, 50, 185, 110, outline="black")
    def draw_body(self):
        self.hangman_canvas.create_line(155, 110, 155, 170, fill="black")
    def draw_left_arm(self):
        self.hangman_canvas.create_line(155, 130, 125, 150, fill="black")
    def draw_right_arm(self):
        self.hangman_canvas.create_line(155, 130, 185, 150, fill="black")
    def draw_left_leg(self):
        self.hangman_canvas.create_line(155, 170, 125, 200, fill="black")
    def draw_right_leg(self):
        self.hangman_canvas.create_line(155, 170, 185, 200, fill="black")
    def draw_face(self):
        self.hangman_canvas.create_line(140, 70, 150, 80, fill="black")
        self.hangman_canvas.create_line(160, 70, 170, 80, fill="black")
        self.hangman_canvas.create_arc(140, 85, 170, 105, start=0, extent=-180, fill="black")
    def guess_letter(self, letter):
        if letter in self.secret_word and letter not in self.correct_guesses:
            self.correct_guesses.add(letter)
        elif letter not in self.incorrect_guesses:
            self.incorrect_guesses.add(letter)
            if self.mode == "race":
                self.update_hangman_canvas()
            else:
                self.attempts_left -= 1
                self.update_hangman_canvas()
        self.update_word_display()
        self.check_game_over()
    def update_word_display(self):
        displayed_word = " ".join([letter if letter in self.correct_guesses else "_" for letter in self.secret_word])
        self.word_display.config(text=displayed_word)
        if self.mode != "race":
            self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")
    def check_game_over(self):
        if set(self.secret_word).issubset(self.correct_guesses):
            self.display_game_over_message("Congratulations, you've won!")
        elif self.mode == "classic" and self.attempts_left == 0:
            self.display_game_over_message("Game over! You have failed!")
        elif self.mode == "race" and self.time_limit == 0:
            self.display_game_over_message("Time's up")
    def display_game_over_message(self, message):
        stylish_font = ("Arial", 18, "italic")
        button_bg = "#4a7a8c"
        button_fg = "white"
        button_font = ("Helvetica", 12, "bold")
        self.reset_button.pack_forget()
        self.buttons_frame.pack_forget()
        self.game_over_label = tk.Label(self.master, text=message, font=stylish_font, fg="red", bg='light blue')
        self.game_over_label.pack(pady=(10, 20))
        if not hasattr(self, 'restart_button'):
            self.restart_button = tk.Button(self.master, text="Reset Game", command=self.reset_game, width=20, height=2, bg=button_bg, fg=button_fg, font=button_font)
        self.restart_button.pack(pady=(10, 20))
    def start_timer(self):
        if self.time_limit:
            self.timer_label.config(text=f"Time left: {self.time_limit}")
            self.master.after(1000, self.update_timer)
    def update_timer(self):
        if self.time_limit > 0:
            self.time_limit -= 1
            self.timer_label.config(text=f"Time left: {self.time_limit}")
            self.master.after(1000, self.update_timer)
        else:
            self.check_game_over()
    def reset_game(self):
        self.master.destroy()
        root = tk.Tk()
        mode_selection = ModeSelectionPage(root)
        root.mainloop()
class Game2048:
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = [[0] * board_size for _ in range(board_size)]
        self.add_new_tile()
        self.add_new_tile()
    def add_new_tile(self):
        empty_cells = [(x, y) for x in range(self.board_size) for y in range(self.board_size) if self.board[y][x] == 0]
        if empty_cells:
            x, y = random.choice(empty_cells)
            self.board[y][x] = random.choice([2, 4])
    def move(self, direction):
        if direction == "left":
            self.move_left()
        elif direction == "right":
            self.move_right()
        elif direction == "up":
            self.move_up()
        elif direction == "down":
            self.move_down()
    def move_left(self):
        for row in self.board:
            self.merge_tiles(row)
    def move_right(self):
        for row in self.board:
            row.reverse()
            self.merge_tiles(row)
            row.reverse()
    def move_up(self):
        for col in range(self.board_size):
            column = [self.board[row][col] for row in range(self.board_size)]
            self.merge_tiles(column)
            for row in range(self.board_size):
                self.board[row][col] = column[row]
    def move_down(self):
        for col in range(self.board_size):
            column = [self.board[row][col] for row in range(self.board_size)]
            column.reverse()
            self.merge_tiles(column)
            column.reverse()
            for row in range(self.board_size):
                self.board[row][col] = column[row]
    def merge_tiles(self, line):
        for i in range(len(line) - 1):
            if line[i] == line[i + 1] and line[i] != 0:
                line[i] *= 2
                line[i + 1] = 0
        for i in range(len(line) - 1):
            if line[i] == 0:
                line[i] = line[i + 1]
                line[i + 1] = 0
class Game2048GUI:
    TILE_COLORS = {
        0: "#CCC0B3", 2: "#EEE4DA", 4: "#EDE0C8", 8: "#F2B179",
        16: "#F59563", 32: "#F67C5F", 64: "#F65E3B", 128: "#EDCF72",
        256: "#EDCC61", 512: "#EDC850", 1024: "#EDC53F", 2048: "#EDC22E"
    }
    def __init__(self, master, board_size=4):
        self.master = master
        self.board_size = board_size
        self.game = Game2048(self.board_size)
        self.tiles = []
        self.create_board()
        self.master.bind("<Left>", lambda _: self.move("left"))
        self.master.bind("<Right>", lambda _: self.move("right"))
        self.master.bind("<Up>", lambda _: self.move("up"))
        self.master.bind("<Down>", lambda _: self.move("down"))
        self.quit_button = tk.Button(self.master, text="Quit", command=self.quit_game)
        self.quit_button.grid(row=self.board_size + 1, columnspan=self.board_size, pady=10)
    def create_board(self):
        for i in range(self.board_size):
            row = []
            for j in range(self.board_size):
                tile = tk.Label(self.master, text="", width=4, height=2, font=("Helvetica", 32), bg="#CCC0B3")
                tile.grid(row=i, column=j, padx=5, pady=5)
                row.append(tile)
            self.tiles.append(row)
        self.update_board()
    def update_board(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                value = self.game.board[i][j]
                self.tiles[i][j].configure(text=str(value), bg=self.TILE_COLORS.get(value, "#CCC0B3"))
    def move(self, direction):
        self.game.move(direction)
        self.game.add_new_tile()
        self.update_board()
    def quit_game(self):
        self.master.destroy()
        root = tk.Tk()
        mode_selection = ModeSelectionPage(root)
        root.mainloop()
def main():
    root = tk.Tk()
    mode_selection = ModeSelectionPage(root)
    root.mainloop()
if __name__ == "__main__":
    main()
