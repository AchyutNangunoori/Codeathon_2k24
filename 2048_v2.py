import tkinter as tk
import random
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
def main():
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
if __name__ == "__main__":
    main()
