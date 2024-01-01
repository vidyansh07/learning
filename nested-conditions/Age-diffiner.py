
class AgeDiffiner:
    def __init__(self):
        try:
            self.age = int(input("Enter your age \n"))
        except ValueError:
            print("Invailid Age")
        else:
            if self.age <= 12:
                print("You'are a Child.")
            elif self.age <= 19:
                print("You'r a Teenager.")
            elif self.age <= 39:
                print("You're a Young Adult.")
            elif self.age <= 59:
                print("You're a Middleager.")
            elif self.age > 59:
                print("You're a Senior Citizen.")
            else:
                print("You're a Goast. ")
        finally:
            print("Thanks for using our AgeDiffiner.")


AgeDiffiner()
