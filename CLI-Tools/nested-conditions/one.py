# procesoral
# def printMyName():
#     x = "saurav"
#     print(x)
# printMyName()

"""
# Exception Handling in python"""

# def app():
# try:
#     num = eval(input(massage))
# except:
#     print("Enter a valid number.")
# except:
#     print("Enter a valid number.")
# else:
#     x = type(num)
#     print(f"your number's type is {x} and your number is {num}")
# finally:
#     print("Thank you for using our app.")


# app()

# def app():
#     try:
#         massage = input("Enter the number \n")
#         num = int(massage)
#     except NameError as nmErr:
#         print(nmErr)
#     except ValueError:
#         print("Please Enter a integer.")
#     except:
#         print("Something went wrong.")


# app()


# def main():
#     massage = input("enter the number \n")
#     num = int(massage)


# main()


# def app():
#     try:
#         massage = int(input("Enter the number \n"))x
#         num = int(massage)
#     except NameError as nmErr:
#         print(nmErr)
#     except ValueError:
#         print("Please Enter a integer.")
#     except:
#         print("Something went wrong.")
#     else:
#         print("your number is ", num)
#     finally:
#         print("Thank you for using our app.")

# class evenOddchecker:
#     def __init__(self):
#         try:
#             self.number = int(input("Enter the number \n"))
#         except ValueError:
#             print("Please enter a number.")
#         else:
#             if self.number % 2 == 0:
#                 print(self.number, "is a Even number.")
#             else:
#                 print(self.number, "is a Odd number.")


# evenOddchecker()

'''
    step 1: start
    step 2: create a class 
    step 3: create a constructor 
    step 4: try: Take input from user and convert it into integer
    step 5: except: show user a report of program
    step 6: else:
                if: self.number % == 0: display number is even
                else: number is odd.
    step 7: class evenOddchecker class
    step 8: end
    
'''


# class NumberGuess :
#     def __init__(self):
#         try: 
#             self.number = int(input("Enter the number:"))
#         except:
#             print("Plese Enter a number")
#         else:
#             if self.number % 2==0:
#                 print(self.number, "number is Even number")
#             else:
#                 print(self.number, "number is odd number")
#         finally:
#             print("Thank you using this app.")
# NumberGuess()

"""


"""

# Guess the number 

# import random

# class GuessNumber :
#     def __init__(self):
#         self.random_num = random.randint(0,100)
#         score=0
#         n=0;
#         while n==0:
#             a=0
#             while a==0:
#                 try:
#                     guess = int(input("Enter your guess: "))
#                 except ValueError:
#                     print("Plese Enter a number")
#                 else:
#                     if guess == self.random_num:
#                         print("Congratulation you got it ")
#                         a=1
#                         score=score+1
#                         print(score)
#                         break
#                     elif guess >self.random_num:
#                         print("Your guess is too high \n Try again")
#                     else:
#                         print("Your guess is smaller than number")
#             print("If you want to continue:Y/N")
#             choice=input('Enter your choice')
#             if choice=='N':
#                 n=1

# GuessNumber()


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