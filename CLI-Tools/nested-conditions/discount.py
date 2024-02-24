class App:
    def __init__(self):
        try:
            gender = input("Enter your Gender : ").lower()

            if gender != "male" and gender != 'female':
                print("plese Enter a valid gender.")
            age = int(input("Enter your age : "))
        except ValueError:
            print("Please a Enter the Data")
        else:
            if gender == "female" and age <= 25:
                print("You're eligible for the coupan.")
            elif gender == "male" and age <= 22:
                print("You're eligible for the coupan.")
            else:
                print("You're not eligible for the coupan.")


App()
