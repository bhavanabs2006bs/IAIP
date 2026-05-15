import tkinter as tk
from tkinter import messagebox

# ---------------- MAIN WINDOW ---------------- #
root = tk.Tk()
root.title("Online Banking System")
root.geometry("800x650")
root.configure(bg="#1e1e1e")

# ---------------- GLOBAL VARIABLES ---------------- #
balance = 0
transactions = []

# ---------------- FUNCTIONS ---------------- #

# Create Account
def create_account():

    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showerror(
            "Error",
            "Please enter username and password"
        )
        return

    messagebox.showinfo(
        "Success",
        "Account Created Successfully!"
    )

# Login Function
def login():

    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showerror(
            "Error",
            "Please enter login details"
        )
        return

    messagebox.showinfo(
        "Login Success",
        f"Welcome {username}"
    )

# Deposit Function
def deposit():

    global balance

    try:
        amount = float(amount_entry.get())

        if amount <= 0:
            messagebox.showerror(
                "Error",
                "Enter valid amount"
            )
            return

        balance += amount

        transactions.append(
            f"Deposited ₹{amount}"
        )

        update_balance()

        messagebox.showinfo(
            "Success",
            f"₹{amount} Deposited Successfully"
        )

    except:
        messagebox.showerror(
            "Error",
            "Invalid Input"
        )

# Withdraw Function
def withdraw():

    global balance

    try:
        amount = float(amount_entry.get())

        if amount <= 0:
            messagebox.showerror(
                "Error",
                "Enter valid amount"
            )
            return

        if amount > balance:
            messagebox.showerror(
                "Error",
                "Insufficient Balance"
            )
            return

        balance -= amount

        transactions.append(
            f"Withdrawn ₹{amount}"
        )

        update_balance()

        messagebox.showinfo(
            "Success",
            f"₹{amount} Withdrawn Successfully"
        )

    except:
        messagebox.showerror(
            "Error",
            "Invalid Input"
        )

# Update Balance
def update_balance():

    balance_label.config(
        text=f"Current Balance: ₹{balance}"
    )

# Show Transactions
def show_transactions():

    transaction_window = tk.Toplevel(root)

    transaction_window.title("Transaction History")
    transaction_window.geometry("400x400")

    text_area = tk.Text(
        transaction_window,
        font=("Arial", 12)
    )

    text_area.pack(fill="both", expand=True)

    if transactions:

        for transaction in transactions:
            text_area.insert(
                tk.END,
                transaction + "\n"
            )

    else:

        text_area.insert(
            tk.END,
            "No Transactions Yet"
        )

# ---------------- TITLE ---------------- #
title = tk.Label(
    root,
    text="ONLINE BANKING SYSTEM",
    font=("Arial", 24, "bold"),
    bg="#1e1e1e",
    fg="white"
)

title.pack(pady=20)

# ---------------- LOGIN FRAME ---------------- #
login_frame = tk.Frame(
    root,
    bg="#2d2d2d",
    padx=20,
    pady=20
)

login_frame.pack(pady=10)

# Username
username_label = tk.Label(
    login_frame,
    text="Username",
    font=("Arial", 14),
    bg="#2d2d2d",
    fg="white"
)

username_label.grid(row=0, column=0, pady=10)

username_entry = tk.Entry(
    login_frame,
    font=("Arial", 14)
)

username_entry.grid(row=0, column=1, pady=10)

# Password
password_label = tk.Label(
    login_frame,
    text="Password",
    font=("Arial", 14),
    bg="#2d2d2d",
    fg="white"
)

password_label.grid(row=1, column=0, pady=10)

password_entry = tk.Entry(
    login_frame,
    show="*",
    font=("Arial", 14)
)

password_entry.grid(row=1, column=1, pady=10)

# Create Account Button
create_button = tk.Button(
    root,
    text="Create Account",
    font=("Arial", 14, "bold"),
    bg="#00cc99",
    fg="black",
    padx=20,
    pady=10,
    command=create_account
)

create_button.pack(pady=10)

# Login Button
login_button = tk.Button(
    root,
    text="Login",
    font=("Arial", 14, "bold"),
    bg="#4da6ff",
    fg="white",
    padx=20,
    pady=10,
    command=login
)

login_button.pack(pady=10)

# ---------------- BANKING FRAME ---------------- #
bank_frame = tk.Frame(
    root,
    bg="#2d2d2d",
    padx=20,
    pady=20
)

bank_frame.pack(pady=20)

# Amount Entry
amount_label = tk.Label(
    bank_frame,
    text="Enter Amount",
    font=("Arial", 14),
    bg="#2d2d2d",
    fg="white"
)

amount_label.grid(row=0, column=0, pady=10)

amount_entry = tk.Entry(
    bank_frame,
    font=("Arial", 14)
)

amount_entry.grid(row=0, column=1, pady=10)

# Deposit Button
deposit_button = tk.Button(
    bank_frame,
    text="Deposit",
    font=("Arial", 14, "bold"),
    bg="#00cc99",
    fg="black",
    padx=20,
    pady=10,
    command=deposit
)

deposit_button.grid(row=1, column=0, pady=15)

# Withdraw Button
withdraw_button = tk.Button(
    bank_frame,
    text="Withdraw",
    font=("Arial", 14, "bold"),
    bg="#ff4d4d",
    fg="white",
    padx=20,
    pady=10,
    command=withdraw
)

withdraw_button.grid(row=1, column=1, pady=15)

# ---------------- BALANCE LABEL ---------------- #
balance_label = tk.Label(
    root,
    text="Current Balance: ₹0",
    font=("Arial", 18, "bold"),
    bg="#1e1e1e",
    fg="#00ffcc"
)

balance_label.pack(pady=20)

# ---------------- TRANSACTION BUTTON ---------------- #
transaction_button = tk.Button(
    root,
    text="Transaction History",
    font=("Arial", 14, "bold"),
    bg="#ffaa00",
    fg="black",
    padx=20,
    pady=10,
    command=show_transactions
)

transaction_button.pack(pady=10)

# ---------------- FOOTER ---------------- #
footer = tk.Label(
    root,
    text="Python Internship Project",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="gray"
)

footer.pack(side="bottom", pady=20)

# ---------------- RUN APP ---------------- #
root.mainloop()