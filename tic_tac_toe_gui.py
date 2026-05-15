import tkinter as tk
from tkinter import messagebox

# ---------------- WINDOW SETUP ---------------- #
root = tk.Tk()
root.title("Advanced Tic Tac Toe")
root.geometry("500x650")
root.configure(bg="#1e1e1e")

# ---------------- VARIABLES ---------------- #
current_player = "X"
board = ["" for _ in range(9)]

x_score = 0
o_score = 0

# ---------------- TITLE ---------------- #
title = tk.Label(
    root,
    text="TIC TAC TOE",
    font=("Arial", 28, "bold"),
    bg="#1e1e1e",
    fg="white"
)
title.pack(pady=20)

# ---------------- SCOREBOARD ---------------- #
score_label = tk.Label(
    root,
    text="Player X: 0   |   Player O: 0",
    font=("Arial", 16, "bold"),
    bg="#1e1e1e",
    fg="#00ffcc"
)
score_label.pack(pady=10)

# ---------------- GAME FRAME ---------------- #
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

buttons = []

# ---------------- CHECK WINNER ---------------- #
def check_winner(player):

    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for positions in win_positions:
        if all(board[pos] == player for pos in positions):
            return True

    return False

# ---------------- UPDATE SCORE ---------------- #
def update_score():
    score_label.config(
        text=f"Player X: {x_score}   |   Player O: {o_score}"
    )

# ---------------- RESET BOARD ---------------- #
def reset_board():

    global board
    global current_player

    board = ["" for _ in range(9)]
    current_player = "X"

    for button in buttons:
        button.config(
            text="",
            state="normal",
            bg="#2d2d2d"
        )

# ---------------- BUTTON CLICK ---------------- #
def button_click(index):

    global current_player
    global x_score
    global o_score

    if board[index] == "":

        board[index] = current_player

        # Button Colors
        if current_player == "X":
            color = "#ff4d4d"
        else:
            color = "#4da6ff"

        buttons[index].config(
            text=current_player,
            fg="white",
            bg=color,
            state="disabled"
        )

        # Winner Check
        if check_winner(current_player):

            if current_player == "X":
                x_score += 1
            else:
                o_score += 1

            update_score()

            messagebox.showinfo(
                "Winner",
                f"🎉 Player {current_player} Wins!"
            )

            reset_board()
            return

        # Tie Check
        if "" not in board:
            messagebox.showinfo(
                "Tie",
                "🤝 Match Draw!"
            )

            reset_board()
            return

        # Switch Player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

# ---------------- CREATE GAME BUTTONS ---------------- #
for row in range(3):

    for col in range(3):

        index = row * 3 + col

        button = tk.Button(
            frame,
            text="",
            font=("Arial", 32, "bold"),
            width=5,
            height=2,
            bg="#2d2d2d",
            fg="white",
            activebackground="#444",
            command=lambda index=index: button_click(index)
        )

        button.grid(
            row=row,
            column=col,
            padx=8,
            pady=8
        )

        buttons.append(button)

# ---------------- RESTART BUTTON ---------------- #
restart_button = tk.Button(
    root,
    text="Restart Game",
    font=("Arial", 16, "bold"),
    bg="#00cc99",
    fg="black",
    padx=20,
    pady=10,
    command=reset_board
)

restart_button.pack(pady=30)

# ---------------- FOOTER ---------------- #
footer = tk.Label(
    root,
    text="Python Internship Project",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="gray"
)

footer.pack(side="bottom", pady=20)

# ---------------- RUN APPLICATION ---------------- #
root.mainloop()