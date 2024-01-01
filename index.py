# def vidyansh():
#     data = eval(input("Enter your number : "))
#     datatype = type(data).__name__
#     print("Your data is", datatype)


# def kttt():s
#     print(54 == "vidaysnh")


# kttt()


# from operator import length_hint


# def Output():
#     data = 'wap'
#     print(len(data))
#     print(data[2])


# Output()

# write a python programm to print the first charecter of string


# def string():
#     string = 'sldfjasljfalsjfsaiofjweioruweo'
#     length = len(string)
#     print(string[length - 1])


# string()


# A small project

# def App():
#     print('Char finder')
#     print("------------")
#     string = input("Enter your word \n")
#     print("Choose an option")
#     print("1. Find the first charecter")
#     print("2. Finde the last charecter")
#     print("3. Find the custom index charecter")
#     option = int(input(""))
#     if option == 1:
#         print(string[0])
#     elif option == 2:
#         print(string[len(string)-1])
#     else:
#         print(string[option-1])


# App()


# Write a program to demonstrate the concept of usage of various operators
# available in python.

# Arithematic operator

# print(2+3)
# print(2-3)
# print(2/3)
# print(2*3)
# print(5 % 4)

# # comparision operator
# 3 == 3
# 3 != 3
# 3 > 1
# 3 >= 3
# 3 < 4
# 3 <= 4

# # logical operator
# ~(2 == 2)  # Logical NOT with ~
# (1 != 1) & (1 < 1)  # Logical AND with &
# (1 >= 1) | (1 < 1)  # Logical OR with |
# (1 != 1) ^ (1 < 1)  # Logical XOR with ^

# a = 5  # Assign a value to a
# x[0] = 1  # Change the value of an item in a list

'''
 Certainly! Conditional statements in Python are used to make decisions in your code based on certain conditions. The most common conditional statements in Python are if, elif (short for "else if"), and else. Here's a simple Python program that demonstrates the use of these conditional statements:
'''

# # conditional statment

# age = int(input("Enter your age: "))
# if age < 18:
#     print("You are a minor.")
# elif age >= 18 and age < 65:
#     print("You are an adult.")
# else:
#     print("You are a senior citizen.")


# # Loop


# print("1. For Loop:")
# for i in range(1, 6):
#     print(i, end=' ')
# print()

# # 2. While Loop
# print("\n2. While Loop:")
# count = 1
# while count <= 5:
#     print(count, end=' ')
#     count += 1
# print()

# index = 0


# def cat():
#     global index
#     index = index+1
#     print(index+1)
#     print('wap institude')
#     if index < 20:
#         cat()


# cat()

# print a table of a number using recursion

# num = 1
# index = int(input("Enter the number"))


# def App():
#     global num
#     num = num+1
#     global index
#     if num <= 10:
#         print(index*num)
#     App()


# App()


# index = 0


# def Table(number):
#     global index
#     index = index+1
#     print(number, "*", index, "=", number*index)
#     if index < 10:
#         Table(number)
#     else:
#         print("Thank you!")


# def App():
#     number = int(input("Enter the number\n"))
#     Table(number)


# App()
# def Output():
#     print('Testing')


# Output()


# write a python program and create a list and print with indexing number

# num = 0


# def list():
#     user = ["vidyansh", "kunal", "Ajay", "shivam", "sakib", 'chotu']
#     global num
#     print(user[num])
#     num = num+1
#     if num < len(user):
#         list()
#     else:
#         print('Thank you')


# list()

# find  a name into a array or list

# index = 0


# def Find(name):
#     User = ["vidyansh", "kunal", "Ajay", "shivam", "sakib", 'chotu']

#     global index
#     data = User[index]
#     if data == name:
#         index = index+1
#         if index < len(User):
#             Find(name)
#             print("name found")
#     else:
#         print("name is not found")


# def Username():
#     app = input("Enter the Name : \n")
#     Find(app)


# Username()

# index = 0


# def Find(name):
#     global index
#     users = ['vidyansh', 'kunal', 'abhinav', 'neer']
#     data = users[index]
#     if data.lower() == name.lower():
#         print("name found")
#     index = index+1
#     length = len(users)
#     if index < length:
#         Find(name)


# def App():
#     userInput = input('Enter your name :\n')
#     Find(userInput)


# App()

# index = 0


# def Find(name):
#     global index
#     users = ['shubham', 'adarsh', 'bishesh', 'abhisek']
#     if users[index] == name:
#         print("Your name is found at", index)
#         index = index+1
#     else:
#         print("Your name is not found")
#     if index < len(users):
#         Find(name)


# def App():
#     userName = input("Enter your username: \n")
#     Find(userName)


# App()

# from lib.result import get, set


# def App():
#     x = 3
#     get(x)


# App()


# def Input():
#     get("my app \n")
#     option = set("Enter Your data \n")
#     get(option)


# Input()


# from time import sleep


# def get():
#     print('one')
#     sleep(3)
#     print("two")


# get()

# from time import sleep
# from lib.result import get, set

# index = 0


# def Get():
#     global index
#     get(index)
#     sleep(1)
#     index = index + 1
#     if index <= 10:
#         Get()
#     else:
#         get("thank you")


# Get()


# Loops in python

# def Main():
#     for index in range(10):
#         user = ['shubham', 'adarsh', 'bishesh', 'abhisek',
#                 'shubham', 'adarsh', 'bishesh', 'abhisek']
#         text = input("Enter your Name: \n")
#         if user[index] == text:
#             print("Your name found at", index+1)
#         else:
#             print("Your name is not in this list")


# Main()

# make a table using loops

# import time


# def Table():
#     num = int(input("Enter the Number : \n"))
#     for i in range(1, 11):
#         print(num, "*", i, '=', num*i)
#         time.sleep(1)


# Table()


# Find the highest number in a list or array

# from time import sleep
# from lib.arrum import max

# def Test():
#     max = 0
#     limit = int(input("Enter your limit: \n"))
#     userInput = []
#     for index in range(limit):
#         data = int(input("Enter your number: \n"))
#         userInput.append(data)
#     print(userInput)
#     for data in userInput:
#         if data > max:
#             max = data
#     print('The maximum number is', max)

# Test()

# from time import sleep
# from lib.arrum import max


# def Test():
#     userInput = []
#     limit = int(input("Enter the limit of array : \n"))
#     for index in range(limit):
#         data = int(input("Enter the number\n"))
#         userInput.append(data)
#     large = max(userInput)
#     print('This is the largest number in the array: ', large)
#     small = min(userInput)
#     print('This is the smallest number in the array: ', small)


# Test()

# def Test():
#     users = ['ram', 'ram@gmail.com', 'mohan', 'shreya',
#              'mohan@gmail.com', 'shreya@gmail.com']


# Dictionary in python

# def GetAmmount(product):
#     discount = product['discount']
#     price = product['price']
#     saveMoney = price*discount/100
#     afterDiscount = product['price'] - saveMoney
#     return {'saved': saveMoney,
#             'ammount': afterDiscount,
#             'discount': discount
#             }


# def App():
#     product = {
#         'title': 'A smart phone',
#         'price': 95999,
#         'currency': '₹',
#         'discount': 17
#     }
#     print(product['title'])
#     ammount = GetAmmount(product)
#     print('The total ammount after the discount ',
#           product['currency'], ammount['ammount'], sep=''   )
#     print('saved ', product['currency'], ammount['saved'], sep='')
#     print('discount ', ammount['discount'], "%", sep='')


# App()

# from prettytable import PrettyTable


# def GetAmmount(product):
#     discount = product['discount']
#     price = product['price']
#     saveMoney = price*discount/100
#     afterDiscount = product['price'] - saveMoney
#     return {'saved': saveMoney,
#             'ammount': afterDiscount,
#             'discount': discount
#             }


# def App():
#     table = PrettyTable()
#     table.field_names = ['Title', 'price', 'discount', 'currency']
#     table.row(['samsung-galexy', 112342, 17, "₹"])
#     table.row(['samsung-galexy', 112342, 17, "₹"])
#     table.row(['samsung-galexy', 112342, 17, "₹"])
#     table.row(['samsung-galexy', 112342, 17, "₹"])
#     table.row(['samsung-galexy', 112342, 17, "₹"])


# App()


# create a datastruce of a family using dictionary and list
# def Main():
#     family = {
#         "person": 'Ramanand Tripathi',
#         'wife': 'Malti Tripathi',
#         'sons': [{
#             'person': 'Vinayak Tripathi',
#             'wife': 'Rina Tripathi',
#             'sons': [
#                 {
#                     'person': 'Vidyansh'
#                 },
#                 {
#                     'person': 'Devansh'
#                 },
#                 {
#                     'person': 'Divyansh'
#                 },
#             ]
#         },
#             {
#             'person': 'Sunil Tripathi',
#             'wife': 'Pargna Tripahi',
#             'sons': [
#                 {
#                     'person': 'vidyansh'
#                 },
#                 {
#                     'person': 'devansh'
#                 },
#                 {
#                     'person': 'divyansh'
#                 },
#             ]
#         }
#         ]

#     }
#     print('Family Tree')
#     print('============================')
#     print(family['person'])
#     print(family['wife'])
#     for son in family['sons']:
#         print(son['person'])
#         print(son['wife'])
#         for son2 in son['sons']:
#             print(son2['person'])

# university = {
#     'name': 'mmdu',
#     'estd': 1993,
#     'chairman': 'lala',
#     'courses': [{
#         'name': 'b-tech',
#         'branches': [{
#             'name':'cse'
#             'sections':[
#                 'name':[

#                 ]
#             ]}
#         ],
#         }
#     ]
# }
# Main()


# procedural oriented programmering

# x = "vidyansh"
# def wap():
#     return "tripathi"
# y = wap()
# print(x, y)


# object oriented programming

# class Object:
#     x = int(input("Enter the first number that you want to sum: "))
#     y = int(input("Enter the second number that your want to sum: "))


# sum = Object()
# print("your sum is", sum.x+sum.y)


# class Main:
#     num1 = 419371973904
#     num2 = 2342398237

#     def object(self):
#         print("Your answer is : ", self.num1+self.num2)


# main_object = Main()
# print(main_object.object())

# class Main:
#     x = 23423

#     def Obj(self, firstNumber, secNumber):
#         return firstNumber+secNumber

#     def Obj2(self):
#         return "Vidyansh"


# print(Main().x, Main().Obj(28, 923), Main().Obj2())

# class Main:
#     result = 0

#     def Add(self, firstNumber, secNumber):
#         self.result = firstNumber+secNumber

#     def output(self):
#         print(self.result)


# main = Main()
# main.Add(56, 2)
# main.output()

# constroctor in oops in python

# class Main:
#     def __init__(self, firstNumber=94832, secondnumber=234):
#         print(firstNumber+secondnumber)


# Main(int(input("Enter the number:")), int(input("Enter the number: ")))

# class Admin:
#     def __init__(self, name="Admin", password="<PASSWORD>"):
#         self.name = "Er Vidyansh"
#         self.email = "Vidyansht@gmail.com"
#         self.username = "vidyansh_07"
#         self.__password = "agtmag"


# admin = Admin()
# print(admin.name)
# print(admin.email)
# print(admin.username)

# oops is a paradime


# class Main:
"""There is x is class or static varible and the y is the Instance varible."""
#     x = "Hello vidyansh"

#     def __init__(self):
#         self.y = "Hello world."

#     def data(self):
#         print("Hello wap!")


# main = Main()
# main.data()
"""
    There is Main() is a Instaces
    try to put instance in a variable.
    Function itself called as Method.
    In Oops variable called as attribute.
    class variable or static varible : a variable or attribute that made in main class.
    Instance varible : a varible that made in constructor with the help of Instance.
    local varible : It is a local variable in a Method.
"""
# from pprint import pprint


# class Data:
#     def __init__(self):
#         self.countries = [
#             {
#                 "name": "INDIA",
#                 "NoOfStates": 28,
#                 "short": "IN",
#                 "code": +91,
#             },
#             {
#                 "name": "UNITED STATES",
#                 "NoOfStates": 50,
#                 "short": "USA",
#                 "code": +1,
#             },
#             {
#                 "name": "UNITED KINGDOM",
#                 "NoOfStates": 4,
#                 "short": "UK",
#                 "code": +44,
#             },
#         ]


# class Main(Data):
#     def __init__(self):
#         super().__init__()
#         pprint(self.countries)
#         pprint("i am vidansh learning the consept of constructor.")


# main = Main()
# main
# data = Data()
# pprint(data.countries)


# class Main:
#     def __init__(self):
#         data = Data()
#         pprint(data.countries)


# Main()

# data = Data()

# for i in range(len(data.countries)):
#     print("This country name is : ", data.countries[i]["name"])
#     print("Short Form :", data.countries[i]["short"])
#     print("No of States", data.countries[i]["NoOfStates"])
#     print("Country code:", data.countries[i]["code"])
#     print("============================================")

"""
# some of the basic consepts are here=
# Constructer their def __init__(self): is  a constructer
# Inheriate : It's a way to use different class of code in different code.

# how to make data private using inheritance and constructor

# from pprint import pprint

"""
# class Data():
#     def __init__(self):
#         self.__contories = [
#             {"name": "INDIA", "NoOfStates": 3, "short": "IND", "code": +91},
#             {"name": "USA", "NoOfStates": 50, "short": "US", "code": +1},
#             {"name": "JAPAN", "NoOfStates": 37, "short": "JP", "code": +81}
#         ]

#     def getContories(self):
#         return self.__contories


# class Main(Data):
#     def __init__(self):
#         super().__init__()
#         pprint(self.getContories())


# main = Main()
"""
# encapsulation is mathod to restrict the use of any class data
"""

# The lambda function

# def Add(x, y, c): return x+y+c
# print(Add(23098, 2340, 2340))

# class Main:
#     def __init__(self):
#         self.add = lambda x, y, z: x+y-z
#         self.multiply = lambda x, y, z: x*y*z
#         self.divide = lambda x, y, z: x*y/z
#         self.substract = lambda x, y, z: x-y-z


# main = Main()
# print(main.add(12, 16, 14))
# print(main.multiply(12, 16, 14))
# print(main.divide(12, 16, 14))
# print(main.substract(12, 16, 14))


"""# Polymorphism : It change the use of object and every functionality according to the place."""

# class Laptop:
#     def dell(self): return 904832
#     def lenovo(self): return 232542
#     def hp(self): return 2323428


# laptop = Laptop()
# print(laptop.dell(), laptop.lenovo(), laptop.hp())


# This is the example of polymorphism

# class Laptop:
#     def __init__(self):
#         print("wap!")

# This is not example of polymorphism
# Laptop()

# =========================================================================================

# class Name:
#     def __init__(self, name):
#         print(name)
# This is one more example of polymorphism

# Name("Vidyansh")
# Name("Devansh")
# Name("Divyansh")

# class Admin:
#     def __init__(self):
#         self.__password = 234324

#     def setPassword(self, password):
#         self.__password = password

#     def getPassword(self):
#         return self.__password


# admin_obj = Admin()
# admin_obj.setPassword(1234)
# print("This is your password :", admin_obj.getPassword())

# mutator or setter  : it's a setting the value of variable.
# accessor or getter   : it's getting the value from variables


# Data Abstarction: It is a mathode to make your data private.

# from new import Convert


# class Main(Convert):
#     def __init__(self):
#         super().__init__()
#         print(self.upperCase("kjkl"))
#         print(self.lowerCase("KDSHFAK;SASKLDFJ"))
#         print(self.sentenceCase("i am vidyansh."))


# Main()

# Data structure and algorithem in python

# write a program to print user input

# class Main:
#     def __init__(self):
#         print("Print your data and start from here!")


# Main()


# def main():
#     userInput = input("Enter Your name : ")
#     print(userInput)


# main()
'''
write a algorithem to print user input
step 1: start
step 2 : Create a function -main
step 3 : Declear a variable -userInput and assign function for taking user input.
step 4 : Call and output function and give UserInput variable to print as output.
step 5 : call app function
step 6 : End
'''


# def Main():
#     x = int(input("Enter your first number: "))
#     y = int(input("Enter your second number: "))
#     z = x + y
#     print(z)


# Main()

# Write a algorithem for this program
'''
    step 1 : start
    step 2 : Create a Main Function 
    step 3 : Create a variable x and take userInput in integer
    step 4 : Create a varibale y and take userInput in integer
    step 5 : Create a varibale z  and assign x+y 
    step 6 : Create a Output function and store the z variable in It.
    step 7 : Get out from the Main function 
    step 8 : Call the Main function 
    step 9 : End 
'''


# def evenOdd():
#     userInput = int(input("Enter the number : "))
#     if userInput % 2 == 0:
#         print("Even number")
#     else:
#         print("Odd number")


# evenOdd()

# Write a algorithem for this code
"""
step 1 : Start
step 2 : Create a function by name evenOdd
step 3 : Create a userInput variable and take and store the integer value in it by the User
step 4 : Use conditional statement if userInput remider's value after diving by 2 is equal to 0
step 5 : Display the expacted output by the Output function
step 6 : Use else keyword and display the unexpacted output by the Output function.
step 7 : exit from evenodd function 
step 8 : call the evenOdd function 
step 9 : end 
"""
