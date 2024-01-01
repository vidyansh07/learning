import random
import tkinter as tk
from tkinter import messagebox

class GuessNumberGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number Game")

        # Styling
        self.master.geometry("400x200")
        self.master.configure(bg="#3498db")

        # Variables
        self.random_num = random.randint(0, 100)
        self.score = 0

        # Widgets
        self.create_widgets()

    def create_widgets(self):
        # Header Label
        header_label = tk.Label(self.master, text="Guess the Number Game", font=("Helvetica", 16), bg="#3498db", fg="white")
        header_label.pack(pady=10)

        # Entry Widget
        self.entry = tk.Entry(self.master, font=("Helvetica", 14))
        self.entry.pack(pady=10)

        # Guess Button
        guess_button = tk.Button(self.master, text="Submit Guess", font=("Helvetica", 12), command=self.check_guess, bg="#2ecc71", fg="white")
        guess_button.pack(pady=10)

        # Reset Button
        reset_button = tk.Button(self.master, text="Reset Game", font=("Helvetica", 12), command=self.reset_game, bg="#e74c3c", fg="white")
        reset_button.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a number")
            return

        if guess == self.random_num:
            self.score += 1
            messagebox.showinfo("Congratulations", f"You got it! Your score: {self.score}")
            self.reset_game()
        elif guess > self.random_num:
            messagebox.showinfo("Too High", "Your guess is too high. Try again.")
        else:
            messagebox.showinfo("Too Low", "Your guess is too low. Try again.")

    def reset_game(self):
        self.random_num = random.randint(0, 100)
        self.score = 0
        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)  # Disable window resizing
    game = GuessNumberGUI(root)
    root.mainloop()