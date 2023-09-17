# def vidyansh():
#     data = eval(input("Enter your number : "))
#     datatype = type(data).__name__
#     print("Your data is", datatype)


# def kttt():
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


# Certainly! Conditional statements in Python are used to make decisions in your code based on certain conditions. The most common conditional statements in Python are if, elif (short for "else if"), and else. Here's a simple Python program that demonstrates the use of these conditional statements:


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

index = 0


def Find(name):
    User = ["vidyansh", "kunal", "Ajay", "shivam", "sakib", 'chotu']

    global index
    data = User[index]
    if data == name:
        index = index+1
        if index < len(User):
            Find(name)
            print("name found")
    else:
        print("name is not found")


def Username():
    app = input("Enter the Name : \n")
    Find(app)


Username()
