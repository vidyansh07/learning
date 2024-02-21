"""
Operation on lists 
    1.Transverse
    2.Deletion
    3.Search
    4.Sort
    5.Insertions    
        
    """

"""Data structure and algorithem
    There are main two type of data structue
    1. linear Ds                         2.Non-linear Ds

    Array                                Binary tree   
    linklist                             Heap
    stack                                Hash Table
    queue                                Graph
    matrix
    
    
    [234,2342,243,45,54,876]
    
    Array : Its a collection of same datatype data(Exeption python) which stores the 
            data in linear form in memory.
            algo : 
                    a[0]: this algo is used in array
                    array : left -> right data storage
    
    Stack : Its depend on algorithem how we write algo for accessing the data from memory
            like stack manner.
            
            algo :
                    stack : top -> bottom
            
            There are two principle for stack
                1. LIFO
                2. FILO
                
                If we follows these principles in array it called stack .
                
                
        Queue : It's a also type of algo which is performed in array for required work

                There are two principle for stack
                1. LILO
                2. FIFO
    
        LinkLists :

        matrix :
    """
    
    
"""
Write a python program to implement stack in data structure
"""

# class Stack:
#     def __init__(self) : # constructor
#         self.data = []
#     def travrce(self):
#         return self.data
#     def isEmpty(self):
#         return self.data == []
#     def push(self,item):
#         self.data.append(item)
#     def remove(self):
#         self.data.pop()
#     def top(self):
#         return self.data[-1]
# stack =Stack()
# stack.push(32)
# print(stack.travrce())


"""Write a python program to check if a string has balanced parentheses using stack"""

# class Ds:
#     def __init__(self):
#         """This is the my way to solve this problem"""
#         # self.string = "{{{}}}"
#         # self.stack=[]
#         # self.stack2= []
#         # for i in range(len(self.string)):
#         #     if i == "{":
#         #         self.stack.append(i)
#         #     elif i == "}":
#         #         self.stack2.append(i)
#         # if len(self.stack)== len(self.stack2):
#         #     print("True")
#         # else:
#         #     print("False")
        
#         """According to sir"""
#         self.stack = []
#     def check(self, string):
#             for char in string:
#                 if char == "(":
#                     self.stack.append(char)
#                 elif char == ")":
#                     if self. stack == [] or self.stack.pop()!="(":
#                         return False
#             return self.stack == []
                
        
        
# ds = Ds()
# print(ds.check("((()))"))


"""Write a program to reverse a string using stack."""

# class Reverse:
#     def __init__(self):
#         self.stack = []
#     def perform(self, string):
#         result = ""
#         for char in string:
#             self.stack.append(char)
#         while self.stack:
#             result = result+self.stack.pop()
#         print(result)
        
    
# reverse = Reverse()
# reverse.perform("Hello")

"""Consept of stacks
    infix Expression:
    postfix Expression:
    prefix Expression:
"""

"""Write a python program to check for stack overflow"""

# class StackOverflow:
#     def __init__(self):
#         self.stack = []
#         self.limit = 5
#     def push (self,data):
            
#             if len(self.stack)<self.limit:
#                 self.stack.append(data)
#             else:
#                 print("Your stack is overflow it can't handle more data")
#             print(self.stack)
# stackoverflow = StackOverflow()

# stackoverflow.push(5)
# stackoverflow.push(5)
# stackoverflow.push(5)
# stackoverflow.push(5)
# stackoverflow.push(5)
# stackoverflow.push(5)

"""Write a program to check the underflow condition in array using stack"""
# class UnderFlow:
#     def __init__(self):
#         self.stack = []
#         self.limit = 0
#     def perform(self):
#             if len(self.stack)>0:
#                 self.stack.pop()
#             else:
#                 print("This is the underflow condition for this array")
# underflow = UnderFlow()
# underflow.perform()

"""find the pelindrom string using stack"""

# class Pelindrom:
#     def __init__(self) :
#         self.stack = []
#         self.reverse = []
        
#     def perform(self,data):
#         for i in data:
#             self.stack.append(i)
#         i =0
#         while i <len(self.stack)+4:
#             self.reverse.append(self.stack.pop())
#             i = i +1
#         if self.stack == self.reverse:
#             print("This is a pelindrom string")
#         else:
#             print("This is not a pelindrom string")
# string = input("Enter the string : ")
# Pelindrom().perform(string)

"""Write a python code for arrage a array in asending order using stack"""

# class Asc():
#     def __init__(self,stack):
#         self.stack = stack
#     def sort (self):
#         temp = []
#         while len(self.stack)!= 0:
#             top = self.stack.pop()
#             while len(temp) !=0 and temp[-1]> top:
#                 self.stack.append(temp.pop())
#             temp.append(top)
#         return temp


# asc= Asc([34,24,63,74])
# print(asc.sort())      


"""Write a program to convert a decimal number to its binary representation using a Stack"""

# class Binary:
#     def __init__(self):
#         self.stack = []
#     def convert(self, num):
#         while num >0:
#             i = num%2
#             self.stack.append(i)
#             num = num //2
#         return self.stack
    
# binary = Binary()
# print(binary.convert(4))


""""""