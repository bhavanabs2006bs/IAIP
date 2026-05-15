import tkinter as tk
import random

# ---------------- GAME SETTINGS ---------------- #
WIDTH = 600
HEIGHT = 600
SPEED = 100
SPACE_SIZE = 20
BODY_PARTS = 3

BACKGROUND_COLOR = "#1e1e1e"
SNAKE_COLOR = "#00ff99"
FOOD_COLOR = "#ff4d4d"
TEXT_COLOR = "white"

# ---------------- WINDOW ---------------- #
root = tk.Tk()
root.title("Advanced Snake Game")

score = 0
direction = "down"

# ---------------- SCORE LABEL ---------------- #
score_label = tk.Label(
    root,
    text="Score: 0",
    font=("Arial", 20, "bold"),
    fg=TEXT_COLOR,
    bg=BACKGROUND_COLOR
)

score_label.pack(fill="x")

# ---------------- CANVAS ---------------- #
canvas = tk.Canvas(
    root,
    bg=BACKGROUND_COLOR,
    width=WIDTH,
    height=HEIGHT
)

canvas.pack()

# ---------------- SNAKE CLASS ---------------- #
class Snake:

    def __init__(self):

        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        start_x = WIDTH // 2
        start_y = HEIGHT // 2

        for i in range(BODY_PARTS):

            self.coordinates.append(
                [start_x - (i * SPACE_SIZE), start_y]
            )

        for x, y in self.coordinates:

            square = canvas.create_rectangle(
                x,
                y,
                x + SPACE_SIZE,
                y + SPACE_SIZE,
                fill=SNAKE_COLOR,
                tag="snake"
            )

            self.squares.append(square)

# ---------------- FOOD CLASS ---------------- #
class Food:

    def __init__(self):

        x = random.randint(
            0,
            (WIDTH // SPACE_SIZE) - 1
        ) * SPACE_SIZE

        y = random.randint(
            0,
            (HEIGHT // SPACE_SIZE) - 1
        ) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(
            x,
            y,
            x + SPACE_SIZE,
            y + SPACE_SIZE,
            fill=FOOD_COLOR,
            tag="food"
        )

# ---------------- CHANGE DIRECTION ---------------- #
def change_direction(new_direction):

    global direction

    if new_direction == "left":
        if direction != "right":
            direction = new_direction

    elif new_direction == "right":
        if direction != "left":
            direction = new_direction

    elif new_direction == "up":
        if direction != "down":
            direction = new_direction

    elif new_direction == "down":
        if direction != "up":
            direction = new_direction

# ---------------- NEXT TURN ---------------- #
def next_turn(snake, food):

    global score

    x, y = snake.coordinates[0]

    # Move Snake
    if direction == "up":
        y -= SPACE_SIZE

    elif direction == "down":
        y += SPACE_SIZE

    elif direction == "left":
        x -= SPACE_SIZE

    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(
        x,
        y,
        x + SPACE_SIZE,
        y + SPACE_SIZE,
        fill=SNAKE_COLOR
    )

    snake.squares.insert(0, square)

    # Food Collision
    if x == food.coordinates[0] and y == food.coordinates[1]:

        score += 1

        score_label.config(
            text=f"Score: {score}"
        )

        canvas.delete("food")

        food = Food()

    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    # Collision Detection
    if check_collisions(snake):

        game_over()

    else:

        root.after(
            SPEED,
            next_turn,
            snake,
            food
        )

# ---------------- COLLISION CHECK ---------------- #
def check_collisions(snake):

    x, y = snake.coordinates[0]

    # Wall Collision
    if x < 0 or x >= WIDTH:
        return True

    if y < 0 or y >= HEIGHT:
        return True

    # Self Collision
    for body_part in snake.coordinates[1:]:

        if x == body_part[0] and y == body_part[1]:
            return True

    return False

# ---------------- RESTART GAME ---------------- #
def restart_game():

    global snake
    global food
    global score
    global direction

    score = 0
    direction = "down"

    score_label.config(
        text="Score: 0"
    )

    canvas.delete("all")

    snake = Snake()
    food = Food()

    next_turn(snake, food)

# ---------------- GAME OVER ---------------- #
def game_over():

    canvas.delete(tk.ALL)

    # Game Over Text
    canvas.create_text(
        WIDTH / 2,
        HEIGHT / 2 - 60,
        text="GAME OVER",
        fill="red",
        font=("Arial", 40, "bold")
    )

    # Final Score
    canvas.create_text(
        WIDTH / 2,
        HEIGHT / 2,
        text=f"Final Score: {score}",
        fill="white",
        font=("Arial", 24, "bold")
    )

    # Try Again Button
    retry_button = tk.Button(
        root,
        text="Try Again",
        font=("Arial", 16, "bold"),
        bg="#00cc99",
        fg="black",
        padx=20,
        pady=10,
        command=restart_game
    )

    canvas.create_window(
        WIDTH / 2,
        HEIGHT / 2 + 70,
        window=retry_button
    )

# ---------------- START GAME ---------------- #
snake = Snake()
food = Food()

# ---------------- KEY CONTROLS ---------------- #
root.bind(
    "<Left>",
    lambda event: change_direction("left")
)

root.bind(
    "<Right>",
    lambda event: change_direction("right")
)

root.bind(
    "<Up>",
    lambda event: change_direction("up")
)

root.bind(
    "<Down>",
    lambda event: change_direction("down")
)

# ---------------- START LOOP ---------------- #
next_turn(snake, food)

# ---------------- RUN APP ---------------- #
root.mainloop()