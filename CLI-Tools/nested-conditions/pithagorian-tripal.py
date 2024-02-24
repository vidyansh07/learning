class PithagorianTripal:
    def __init__(self):
        try:
            a = int(input("Enter the value of a \n"))
            b = int(input("Enter the value of b \n"))
            c = int(input("Enter the value of c \n"))
        except ValueError:
            print("Please enter a integer.")
        else:
            if a ** 2 + b ** 2 == c ** 2:
                print("This is a pithagorian tripal.")
            else:
                print("This is not a pithagorian tripal.")
        finally:
            print("Thanks for using our app.")


PithagorianTripal()
