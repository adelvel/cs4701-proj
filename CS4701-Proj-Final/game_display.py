from tkinter import Frame, Label, CENTER

import game_ai
import game_functions

EDGE_LENGTH = 400
CELL_COUNT = 4
CELL_PAD = 10


UP_KEY = "'w'"
DOWN_KEY = "'s'"
LEFT_KEY = "'a'"
RIGHT_KEY = "'d'"
AI_KEY = "'q'"
AI_PLAY_KEY = "'p'"

LABEL_FONT = ("Verdana", 40, "bold")
LABEL_FONT_2 = ("Verdana", 25, "bold")
GAME_OVER_FONT = ("Helvetica", 48, "bold")
GAME_COLOR = "#a39489"

EMPTY_COLOR = "#c2b3a9"

TILE_COLORS = {
    2: "#daeddf",
    4: "#9ae3ae",
    8: "#6ce68d",
    16: "#42ed71",
    32: "#17e650",
    64: "#17c246",
    128: "#149938",
    256: "#107d2e",
    512: "#0e6325",
    1024: "#0b4a1c",
    2048: "#031f0a",
    4096: "#000000",
    8192: "#000000",
}

LABEL_COLORS = {
    2: "#011c08",
    4: "#011c08",
    8: "#011c08",
    16: "#011c08",
    32: "#011c08",
    64: "#f2f2f0",
    128: "#f2f2f0",
    256: "#f2f2f0",
    512: "#f2f2f0",
    1024: "#f2f2f0",
    2048: "#f2f2f0",
    4096: "#f2f2f0",
    8192: "#f2f2f0",
}


class Display(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title("2048")
        self.master.bind("<Key>", self.key_press)

        self.commands = {
            UP_KEY: game_functions.move_up,
            DOWN_KEY: game_functions.move_down,
            LEFT_KEY: game_functions.move_left,
            RIGHT_KEY: game_functions.move_right,
            AI_KEY: game_ai.ai_move,
        }

        self.grid_cells = []
        self.build_grid()
        self.init_matrix()
        self.draw_grid_cells()

        self.mainloop()

    def build_grid(self):
        background = Frame(
            self, bg=GAME_COLOR, bd=3, width=EDGE_LENGTH, height=EDGE_LENGTH
        )
        background.grid(pady=(140, 0))

        for row in range(CELL_COUNT):
            grid_row = []
            for col in range(CELL_COUNT):
                cell = Frame(
                    background,
                    bg=EMPTY_COLOR,
                    width=EDGE_LENGTH / CELL_COUNT,
                    height=EDGE_LENGTH / CELL_COUNT,
                )
                cell.grid(row=row, column=col, padx=CELL_PAD, pady=CELL_PAD)
                t = Label(
                    master=cell,
                    text="",
                    bg=EMPTY_COLOR,
                    justify=CENTER,
                    font=LABEL_FONT,
                    width=5,
                    height=2,
                )
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)

        # make score header
        # score_frame = Frame(self)
        # score_frame.place(relx=0.5, y=57, anchor="center")
        # Label(score_frame, text="Score", font=LABEL_FONT).grid(row=0)
        # self.score_label = Label(score_frame, text="0", font=LABEL_FONT)
        # self.score_label.grid(row=1)

        # make 4701 ai header
        ai_frame = Frame(self)
        ai_frame.place(relx=0.17, y=45, anchor="s")
        Label(ai_frame, text="CS4701 GAIme", font=LABEL_FONT_2).grid(row=0)

        netid_frame = Frame(self)
        netid_frame.place(relx=0.93, y=45, anchor="s")
        Label(netid_frame, text="dav83", font=LABEL_FONT_2).grid(row=0)

    def init_matrix(self):
        self.matrix = game_functions.initialize_game()

    def draw_grid_cells(self):
        for row in range(CELL_COUNT):
            for col in range(CELL_COUNT):
                tile_value = self.matrix[row][col]
                if not tile_value:
                    self.grid_cells[row][col].configure(text="", bg=EMPTY_COLOR)
                else:
                    self.grid_cells[row][col].configure(
                        text=str(tile_value),
                        bg=TILE_COLORS[tile_value],
                        fg=LABEL_COLORS[tile_value],
                    )
        self.update_idletasks()

    def key_press(self, event):
        score = 0
        valid_game = True
        key = repr(event.char)
        if key == AI_PLAY_KEY:
            move_count = 0
            while valid_game:
                self.matrix, valid_game, newScore = game_ai.ai_move(self.matrix)
                score += newScore
                if valid_game:
                    self.matrix = game_functions.add_new_tile(self.matrix)
                    self.draw_grid_cells()
                    # self.score_label.configure(text=score)
                move_count += 1
        if key == AI_KEY:
            self.matrix, move_made, newScore = game_ai.ai_move(self.matrix)
            score += newScore
            if move_made:
                self.matrix = game_functions.add_new_tile(self.matrix)
                self.draw_grid_cells()
                # self.score_label.configure(text=score)
                move_made = False

        elif key in self.commands:
            self.matrix, move_made, newScore = self.commands[repr(event.char)](
                self.matrix
            )
            score += newScore
            if move_made:
                self.matrix = game_functions.add_new_tile(self.matrix)
                self.draw_grid_cells()
                move_made = False

        # self.score_label.configure(text=newScore)

    def winner_label(self):
        print("got here to label")
        if game_functions.check_for_win(self.matrix):
            game_over_frame = Frame(self, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            Label(
                game_over_frame,
                text="You win!",
                bg="#ffcc00",
                fg="#ffffff",
                font=GAME_OVER_FONT,
            ).pack()
        elif (
            not any(0 in row for row in self.matrix)
            and not game_functions.horizontal_move_exists(self.matrix)
            and not game_functions.vertical_move_exists(self.matrix)
        ):
            print("got here")
            game_over_frame = Frame(self, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            Label(
                game_over_frame,
                text="You lost!",
                bg="#ffcc00",
                fg="#ffffff",
                font=GAME_OVER_FONT,
            ).pack()


def main():
    Display()


if __name__ == "__main__":
    main()
