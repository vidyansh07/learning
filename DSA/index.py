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


# conditions in python 

# def case():
#     string = input("Enter your string :")
#     for i in string:
#             if i.isupper():
#                 print (i +" is uppercase")
#             else: 
#                 print(i + " is lowercase")
# case()

"""Write a python  programm that asks the user for their age and gender and prints a massage indiavting whether they
eligible for a discount . Females under the age of 25 and males under the age of 22  are eligible for a discount."""

# def discount(): 


#     try:
#         gender = input("Enter your gender : ")
#         age = int(input("Enter the numeber : "))
#         if gender.lower() != 'male'or gender.lower()!= 'female':
#             print("Plese select write type of gender")
#     except: 
#         print ("Please Enter right answers")
    
#     else:   
#         if gender.lower()  == 'male' and age <22:
#                 print("you're eligible for this Discounts. ")
#         elif  gender.lower == 'female'and age <25:
#             print("You're eligible")
#         else: 
#             print("You are not eligible for the discount")
            
# discount()


"""Write a program that takes a number from the user and checks if it's a prime numbe grater than 1 and divisible 
by 1 and itself and not divisible by other numbers."""

# def primeNumber():
#     try: 
#         num = int(input("Enter the number: "))
#     except:
#         print("Invalid number")
#     else:
#         if  num > 1:
#             for i in range(2,num):
#                 if  num % i ==0:
#                     print(num , "is not a prime number")
#                     break
#                 else:
#                     print(num, "is a prime number")
#                     break
#             else:
#                 print('not a prime number')

# primeNumber()

# """
#         Write a program that takes a list of numbers and return the sum of all the even numbers in the list.
#     """

# def addEven():
#     a = [23,234,234,234,32,3245]
#     n=0
#     for i in a :
#         if i %2 ==0:
            
#             n= n+i
#     print(n)
# addEven()


"""
    Write  a program that takes a list of strings and reaturns the longest string in the list.
"""

# def stringLengthCounter():
#     strings = ["Hello","Vidyansh","You","are","Learning python"]
    
#     i =1
#     for (j =0, j>len(strings), j++):
#     for string in strings:
        
#         if len(string[i])> len(string):
#                 print(string)

# stringLengthCounter()

# def longString():
#     long = ''
#     strings = ["Hello","Vidyansh","You","Learning python","are","Hello i am vidyansh tripathi"]
#     for string in strings:
#         longLength = len(long)
#         if  len(string) >longLength:
#             long= string
            
#     print(long)
# longString()


# """Write a programm to print reverse string :
#     """
    
# def reverseString():
#     a = input("Enter a string: ")
#     for i in range(len(a)-1,-1,-1):
#         print(a[i]  ,end = "")
# reverseString()

"""
    Write a program that takes a list of numbers and returns a new list with all the numbers squared.
"""
# def squareValue():
#     square_list = []
#     num_list = [23,23,5,2,3]
#     for num in num_list:
#         square_list.append((num**2))
#     print(square_list)
# squareValue()

"""
Write a program that takes a list of numbers and returns the average of all the numbers in the list.
"""

# def average():
#     num_list = []
#     list_limit = int(input("Enter the legth of string: "))
#     for i in range(list_limit):
#         num= int(input(f"Enter the numbers {i+1} :"))
#         num_list.append(num)
#     num = 0
#     for j in num_list:
#         num = num+j
#     print(num/len(num_list))
        
    
    
# average()
    
    
"""Write a program that takes two lists and return a new list with only the elements that are common to bot lists.
    """

# def commonElement():
#     list1 = ["vidyansh","Deevyansh", "Devansh"]
#     list2 = ["rohan", "vidyansh"]
    
    
#     for i in list1:
#         for j in list2:
#             if i == j:
#                 print(i)
# commonElement()

# """Write a program that takes a list of strings and returns a new
#     list with only the strings that contain the
#     letter input by user.
# """
# def charInString():
#     a = ["Hello", "Vidyansh", "Vaibhav"]
#     char = input("Enter the char : ").lower()
#     for i in a:
#         if char in i:
#             print(i)
# charInString()

"""Their is a array i have to find the fourth smallest element of array"""
# def reverse():
#     a = [12,23,54,3,53,32]
#     count = []
#     i = 1
#     for i in range(len(a)-1):
#         i = i+1
#     for j in a:
#         if j<a[i]:
#             count.append(a[i-1])
#     print(count)
# reverse()


# """
# Restart app
# """  
# def restart():
#     value = input("Enter the value : ")
#     if value.lower() == "exit" :exit()
    
# while True: 
#     restart()

"""
    Write a python program for factorials
"""
# def factorials():
    
#     try :
#         value = int(input("Enter the number : "))
#     except:
#         print("Please Enter the write values")
#     else:
#         i = 1
        
#         while value >= 1:
#             i = i * value
#             value= value-1
#         print(i)
# factorials()
    
    
"""
    Write a program to reverse a array
"""
# def reverse():
#     b = []
#     a = [2,43,54,586,45,765,867]
#     for i in range(len(a)-1,-1,-1):
#         print(a[i])
# reverse()

"""
    Write a python program to count the number of digits in a given integers
"""
# def count():
#     try:
#         a = int(input("Enter the number : "))
#     except:
#         print("Please input the Integer Value")
#     else:
#         b = str(a)
#         print(len(b))
# count()


# def count():
#     i=0
#     a = int(input("Enter the Number : "))
#     while a>0:
#         a= a//10
#         i = i+1
        
#     print(i)
# count()

"""Write a Python program to print the Fibonacci sequence up to a given number using Fabonaci serise"""

# def fabonacci():
#     try: value = int(input("Enter the number : "))
#     except: print("Invalid Number")
#     else:
#         start_0 =0
#         start_1 =1
#         result =0
#         while start_1<value:
#             result = start_0 + start_1
#             print(result)
#             start_0 =start_1
#             start_1 = result
        
# fabonacci()

"""
    Write a program to guess the number :
"""
# import random

# def guess():
    
#         num = random.randint(0,100)
#         i =1
#         while  i:
#             try:
#                 choice = int(input("Enter the number : "))
#             except:
#                 print("Please Enter the write choice : ")
#             else:
                
#                 if num > choice:
#                     print("Your number is small.")
#                 elif num <choice:
#                     print("Your number is greater.")
#                 else:
#                     print("Congratulations ! You got the number.")
#                     i = 0
# guess()

"""Write a program to find the root of quadratic equation"""


# import math
# def equation():
#     print("This the solution of quadratic equations \n please Enter the values is form of ax^2 +bx + c. \n \n Thank You")
    
#     try :
#         a = float(input("Enter the value of a :"))
#         b = float(input("Enter the value of b :"))
#         c = float(input("Enter the value of c :"))
#     except:
#         print("Please Enter the write Values of a, b, c ")
#     else:
#         discriminent = b**2 -4*a*c
#         if discriminent > 0:
#             x1 =(-b+math.sqrt(b*b -4*a*c))/2*a
#             x2 =(-b-math.sqrt(b*b -4*a*c))/2*a
#             print("First Value of x is ",x1)
#             print("Second Value of x is ",x2)
#         else:
#             print("We can not find the value of this equations.")

# equation()       


"""Write a python program that uses a while loop to remove all occurrence of a give element from a list"""

# def removeFromList():
#     a = [43,324,13,12,43]
#     value = int(input("Enter the Number :"))
#     # for i in a:
#     #     if i == value:
#     #         a.remove(i)
#     # print(a)
    
# removeFromList()  


"""Write a python program that uses a while loop to convert a decimal number to its binary equivalent"""
# def binary():
#     try : 
#         num = int(input("Enter the number : "))
#     except:
#         print("Please Enter the write value")
#     else:
#         b = ""
#         d = num
#         while d>0:
#             b =b+ str(d % 2)
#             d = d //2 
#         print(f" {b} is binary of {num}")
# binary()

"""Write a python program tha t uses a while loop to find the frequency of each element in a given list"""
# def frequency():
#     nums = [9,0,3,2,4,2,3,6,7,7,3]
#     i = 0 
#     counter = {}
#     while i<len(nums):
#         a = nums[i]
#         if a in counter:
#             counter[a]=counter[a]+1
#         else:
#             counter[a]=1
#         i = i+1
#     print(counter)
#     for i in counter:
#         if counter[i] == 1:
#             print(i, "is 1 time in the list")
# frequency()


# def pattern():
#     a = "*"
#     x =6
#     y =2
#     for i in range(x):
#         for j in range(2):
#             if i 
# pattern()


# """Bit manupilations"""

# def singleElement():
#     a = []
#     length = int(input("Enter the length of arrey : "))
    
#     for i in range(length):
#         elements = int(input("Enter the elements : "))
#         a.append(elements)
#     i = 0
#     while i <=len(a): 
#         a= a^a[i]  
#         i +=i
# singleElement()
    

"""Lets make a  char find in a string"""

# class CharFinder():
#     def __init__(self, string,input):
#         self.string = string
#         for i in self.string:
#             if i.lower() == input:
#                 name = "char found"
#                 print(name)
        
# char = CharFinder("Hello","e")
# char


"""Write a python program to count the number of upper and lower cases in a string"""

# def counter():
#     upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     lower = upper.lower()
#     num_u = 0
#     num_l = 0
#     a = input("Enter the string : ")
#     for i in range(len(a)):
#         if a[i] in upper:
#             print(f"{a[i]} is a upper case")
#             num_u = num_u+1
#         elif a[i] in lower:
#             print(f"{a[i]} is in lower case")
#             num_l += 1
#     print(f"In this string {num_u} upper case letters and {num_l} lower case letters")
# counter()

"""Write a python program to accept a string a display it back after 
removing alternate charecters from it
"""

# def alternate():
#     a = input("Enter the string :")
#     pass
    
# alternate()

"""Write a python to pelindrom """
# def pelindrom():
#     a = input("Enter a String : ")
#     reverse = a[::-1]
#     if a == reverse: print("this is pelindrom")
#     else: print("This is not a pelindrom")
# pelindrom()

"""Write a python code for count the number of word in a string """
# def count():
#     a = input("Enter the string : ")
#     print(len(a))
# count()

"""Write a program to print the reverse of the string : """

# def reverse():
#     a = input("Enter the string")
#     b= ""
#     for i in range(len(a)):
#         b= b +a[-i-1]
#     print(b)
# reverse()

"""Write a program to check if string contains all letters of alphabet"""

# def alphabet():
#     a = input("Enter the string : ")
#     b = "abcdefghijklmnopqrstuvwxyz"
#     for i in b :
#         if i not in a:
#             print("This string contains not all charecters of english alphabet")
#             break
# alphabet()

"""Write a code for armstrong number."""

# def armstrongNum(num):
#     x = []
#     z = str(num)
#     y= 0
#     for i in range(len(z)):
#         x.append(z[i])
#     print(x)
#     for j in range(len(x)) :
#         y = y +int(x[j])**3
#     print(y)
#     if y == num:
#         print(f"{num} is a armstrong number.")
#     else:
#         print(f"{num } is not a armstrong number.")
# armstrongNum(153)

"""second method"""

# def is_armstrong_number(number):
#     num_str = str(number)
#     num_digits = len(num_str)
#     sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)
#     return sum_of_digits == number

# # User input
# num = int(input("Enter a number: "))

# # Check and display the result
# if is_armstrong_number(num):
#     print(f"{num} is an Armstrong number.")
# else:
#     print(f"{num} is not an Armstrong number.")

"""Problem Statement - Create a Python program that prompts the user to enter positive numbers continuously. The program should use a while loop to collect input data until the user enters a non-positive number. Implement simple data validation to ensure entered values are valid positive numbers. Finally, output the list of positive numbers entered by the user. The objective is to create an interactive and error-tolerant program for collecting and handling user input."""

# def positiveNumber():
#     x = []
#     i=1
#     while i:
#         num = int(input("Enter the Positive number to continue the game : "))
        
#         if num >0:
#             x.append(num)
#         else:
#             print(x)
#             i =0
        
# positiveNumber()
        
"""Second approch"""
# numbers = []

# while True:
#     user_input = input("Enter a positive number (enter a non-positive number to stop): ")

#     # Check if the input can be converted to a float and is non-negative
#     if user_input.replace('.', '', 1).isdigit() and float(user_input) > 0:
#         numbers.append(float(user_input))
#     elif user_input.replace('-', '', 1).isdigit() and float(user_input) <= 0:
#         break  # Exit the loop if a non-positive number is entered
#     else:
#         print("Invalid input. Please enter a valid positive number.")

# # Data handling after the loop
# if numbers:
#     print(f"You entered the following positive numbers: {numbers}")
# else:
#     print("No positive numbers were entered.")

"""Write a code for adding two small numbers from a list of numbers"""
# def sum_two_smallest_numbers():
#     numbers= [3,24,53,2,424,643]
#     x = numbers
#     y = []
#     for i in range(len(numbers)):
#     # write a code for sort the array in minimum to highest
#         for j in range(len(numbers)):
#             if numbers[i]>= numbers[j]:
#                 y.append(numbers[i])
#     z = y[0]+y[1]
#     print(z)
#     print(y)
# sum_two_smallest_numbers()

"""Make the pascal trangle"""

# def pascal_trangle():
#     print(1)
#     k=1
#     for i in range(1,6):
#         for j in range(3):
#             print(" ")
#         for j in range(1,i+1):
#             print(j,end="  ")
#         print(k)

# pascal_trangle()

"""print the 1 to 9 for infinity"""

# def oneToNine():
#     i=0
#     while i<9:
#         name = input()
#         i = i+1
#         print(i)
#         if i ==9:
#             i=0
# oneToNine()

"""write a program to find the perfect square"""
# def find_next_square(sq):
#     # Return the next square if sq is a square, -1 otherwise
#     x=sq**0.5
    
#     if int(x)==float(x):
#         S = (x+1)**2
#         S = int(S)
#         return S
#     else:
#         return -1
    
# print(find_next_square(121))
# print(23==23.00)

"""Rock Paper scissors"""
"""Their is a mistake"""
# class Game:
#     def __init__(self, p1,p2):
#         if p1==p2:
#             print("Game drawing")
#         elif p1=="rock" and p2=="paper" or p1=='paper' and p2=='rock':
#             print("p1 wins")
#         elif p1=="paper" and p2=="scissors" or p1=='paper' and p2=='scissors':
#             print("p2 wins")
#         elif p1=="scissors" and p2=="rock" or p1=='rock' and p2 == 'scissors':
#             print("p2 wins")

# game = Game('paper', 'rock')
# game

# coding ='coding'
# love =coding
# love
# print(love)

"""Count and speak problems"""
# def count(n, string):
#     count = 0
#     for i in range(len(string)):
#             count += 1
#             if string[i]!= string[i-1]:
#                 count=1
#             if string[i]>=string[i-1]:
#                 x =str(count)+str(string[i])
#                 print(x ,end = '')

# count(4,"2112")

"""solveing linear equations"""
# def solve():
#     print('The formate of equations should be look like this: \n ax + by = c\n where a, b and c are constents.')

    
#     try:
#         a = input("Enter the equation 1 :")
#         b = input("Enter the equation 2 :")
#     except:
#         print(
#             "please enter the equation correctly"
#         )
#     else:
#         a= a.strip().lower()
#         b= b.strip().lower()
#         x = []
#         y = []
#         for i in a:
#             if type(i)== str(i):
#                 x.append(i)
#             else:
#                 x.append(i)
#         for i in b:
#             if type(i)== str(i):
#                 y.append(i)
#             else:
#                 y.append(i)
#         print(x)
#         print(y)
        
# # solve()

# """Vehicals and wheels questions"""
# def solve():
#     a = int(input("Enter the numbers of wheels : ") )
#     b = int(input("Enter the  number of vehicles to want to produce : ") )
    
#     x = a//2
#     y = a//4
#     if x+y ==b:
#         print(x,y)
# solve()

"""matrix chain multiplication problemhv"""
   

# import sys
 

# def MatrixChainOrder(p, i, j):
#     if i == j:
#         return 0
 
#     _min = sys.maxsize

#     for k in range(i, j):
 
#         count = (MatrixChainOrder(p, i, k)
#                  + MatrixChainOrder(p, k + 1, j)
#                  + p[i-1] * p[k] * p[j])
 
#         if count < _min:
#             _min = count
 
#     return _min
 
 

# if __name__ == '__main__':
#     arr = []
#     numberOfnums = int(input("Enter how many numbers you want to insert : "))
   
#     for i in range(numberOfnums+1): 
#         nums= int(input("Enter the numbers :"))
#         arr.append(nums)
        
    
#     N = len(arr)
     
#     print("Minimum number of multiplications is ",
#       MatrixChainOrder(arr, 1, N-1))


"""Delete the first element of a stack of numbers"""

# def stack():
#     params = []
#     length_of_arr = int(input("Enter the number : "))
    
#     for i in range(length_of_arr):
#         num = int(input("Enter the number:"))
#         params.append(num)
#     print(params)
#     stack = []
#     for i in range(1,len(params)):
#         stack.append(params[i])
#     print(stack)

# stack()

"""Solve a factorial with recursion"""

# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n * factorial(n-1)

# print(factorial(5))


"""Pop a bottom element from the stack using recursion"""

# def stack():
#     params = []
#     length_of_arr = int(input("Enter the number : "))
    
#     for i in range(length_of_arr):
#         num = int(input("Enter the number:"))
#         params.append(num)
#     print(params)


"""Dishiktrash algorithm"""
   
# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph
class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
 
    def printSolution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])
 
    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):
 
        # Initialize minimum distance for next node
        min = 1e7
 
        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index
 
    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):
 
        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)
 
            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[u] = True
 
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                   sptSet[v] == False and
                   dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
 
        self.printSolution(dist)
 
# Driver program
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]
 
g.dijkstra(0)
 
# This code is contributed by Divyanshu Mehta