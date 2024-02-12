# class Addtion :
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def add(self):
#         return self.a + self.b
#     def __str__(self):
#         return "Addtion of two numbers is : " + str(self.add())


# addtion  = Addtion(14,16)
# print(addtion)


# class Name:
#     def __init__(self, name):
#         self.__name = name
#     def __str__(self):
#         return "Name is : " + self.__name

# name = Name("Rahul")

# name = Name.
# print(name)


# class Countories :
#     def __init__(self, contories):
#         self.Countries= [
#             "India",
#             "USA",
#             "UK",
#             "China",
#             "Japan"
#         ]


#         self.countory = countory
#     def __str__(self):
#         return "Name is : " + self.Countories + " Countory is : " + self.countory

# countory = Countories("India")

# """Write a program to count vowel in the in given string and return the number of vowels from string"""
# def countVowel():
#     string = input("Enter the string : ")
#     vowel = "aeiou"
#     j = 0
#     for i in string:
#         if i.lower() in vowel:
#             j = j +1
        
#     print(j)


# countVowel()

"""Find the largest number from given list"""
# def largestNum():
    
#     a = [32,23,53,23,235]
    
#     for i in range(len(a)-1):
#         if a[i+1]-a[i]>=0:
#             print(a[i+1])
# largestNum()

# def largeNum():
#     a = [2,324,234,234,2342]
#     print(max(a))
# largeNum()

# def largNum():
#     a = 0
#     nums = [23,234,54,7645]
#     for num in nums:
#         if num >a:
#             a = num
#     print(a)
# largNum()

"""Smallest number finder"""

# def smallNum():
#     nums = [21,213,123,54,745]
#     min = nums[0]
#     for num in nums:
#         if num > min:
#             num = min
#     print(num)
    
# smallNum()

# """Write a program to find the second largest numbser from the list"""

# def secondLarge():
#     a = [23,234,24325,234]
#     large = max(a)
#     sl = a[0]
#     for num in a:
#         if num > sl and num <large:
#             sl = num
#     print("Second largest variable in list ", sl)

# secondLarge()

"""Write a program for pelindrom string"""

# def pelindrom():
#     a = input("Enter the string : ")
#     for i in range(len(a)):
#         if a[i] == a[-(i+1)]:
#             output = "This is a pelindrom string"
#         else:
#             output = "This is not a pelindrom string"
#     print(output)
# pelindrom()

# def pelindrom():
#     a = input("Enter a String : ")
#     reverse = a[::-1]
#     if a == reverse: print("this is pelindrom")
#     else: print("This is not a pelindrom")
# pelindrom()


"""Write a program to print a new prime number list from the list of random numbers"""

# def primeNumber():
#     b = []
    # a = []
    # item = int(input('Enter the numbers of Elements that you want to insert :'))
    
    # for i in range(item): # type: ignore
    #     nums = int(input("Enter the numbers : "))
    #     a.append(nums)
    
#     for i in a:
#         if i >1:
#             for index in range(2,i):
#                 if i % index ==0: break
#             else:
#                 b.append(i)
#     print(b)
# primeNumber()

 
"""Write a program that takes a list of numbers and returns a new list with only the numbers divisible by 3"""

# def divisible():
#     a = []
#     b = []
#     item = int(input('Enter the numbers of Elements that you want to insert :'))
    
#     for i in range(item):
#         try: 
#             nums = int(input("Enter the numbers : "))
#         except:
#             raise Exception("Invalid number")
#         else:
#             a.append(nums)
    
#     for i in a:
#         if i %3 ==0:
#             b.append(i)
#     print(b)
            
# divisible()

# """Write a program that takes a list of string string and return the string in uppercase"""
# def upperList():
#     list_1 = ["vidyansh","hello"]
#     list_2 = []
#     upper = list_1.upper()
#     for i in list_1:
#         list_2.append(upper)
#     print(list_2)
        
        
# upperList()

"""Write a program that takes the string and count the charectors init>"""

# def count():
#     a = input("Enter the string : ")
#     stringList =a.split(" ")
#     count = len(stringList)
#     print(count)    
# count()

"""Write a program that takes a list of strings and returns a new list that contains all strings that starts with a"""
# def letterString():
#     mainList = []
#     letterList = []
#     lengthOfList = int(input("Enter the number of string that you want to insert: "))
#     letter = input("Enter the letter you want to search : ")
#     for i in range(lengthOfList):
#         strings = input(f"Enter the string {i+1} : ")
#         mainList.append(strings)
    
#     for i in mainList:
#         if i[0].lower   == letter:
#             letterList.append(i)
#     print(letterList)

# letterString()

