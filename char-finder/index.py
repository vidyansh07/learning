~# def firstNumber():
#     print('First Charecter is ', string[0])


# def secondNumber():
#     print('Last Charecter is ', string[len(string)-1])


# def customNumber():
#     index = int(input("Enter your custom number\n"))
#     length = len(string)
#     if length >= index:
#         print('Your custom Charecter is ', string[index-1])
#     else:
#         print("invalid command")


# def App():
#     print('Char finder')
#     print('-----------------')
#     global string
#     string = input("Enter your string\n")
#     print('choose in given options')
#     print('1. Find the first charecter')
#     print('2. Find the second charecter')
#     print('3. Find the custom charecter')
#     option = int(input(''))
#     if option == 1:
#         firstNumber()
#     elif option == 2:
#         secondNumber()
#     elif option == 3:
#         customNumber()


# App()





# def firstChar() : 
#     return string[0]
# def lastChar(): 
#     return string[-1]
# def customChar():
#     num = int(input("Enter the number you want to access."))
#     try:
#         return string[num-1]
#     except IndexError:
#         return ("Invalid Input! Please enter a valid number.")


# def charFinder () :
#     print("Welcome to char-finder")
#     print("------------------------------------------")
#     global string
#     string = input("Enter your string\n")
#     print('choose in given options')
#     print('1. Find the first charecter')
#     print('2. Find the second charecter')
#     print('3. Find the custom charecter')
#     option = input("")
#     if option =="1":
#         print('The first character of the string is',firstChar())
#     elif option == "2":
#         print('The last character of the string is',lastChar())
#     elif option=="3":
#         print("Your given costum number is ",customChar())

# charFinder()