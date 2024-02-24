# class Case:
#     def __init__(self):
#         string = input("Enter a String :\n")
#         for char in string:
#             if char.isupper():
#                 print(
#                     f"{char} is in uppercase.")
#             elif char.islower():
#                 print(
#                     f"{char}  is in lower case.")


# Case()

# class Case:
#     def __init__(self):
#         capital = True
#         small = False
#         string = input("Enter a String :\n")
#         for char in string:
#             if char.isupper():
#                 capital = True
#             else:
#                 small = True
#         if capital == True and small == True:
#             print("String both contains lower and upper Case chrecters.")
#         else:
#             if capital == True and small == False:
#                 print("String only contains UpperCase letters")
#             else:
#                 print("String only contains LowerCase letters")


# Case()

"""class Case:
    def __init__(self):
        string = input("Please Enter a String :")
        capital = any(char.isupper() for char in string)
        small = any(char.islower() for char in string)
        if capital == True and small == True:
            print("String both contains lower and upper Case chrecters.")
        else:
            if capital == True and small == False:
                print("String only contains UpperCase letters")
            else:
                print("String only contains LowerCase letters")


Case()"""
