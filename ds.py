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

class Stack:
    def __init__(self) : # constructor
        self.data = []
    def isEmpty(self):
        return self.data == []
    def push(self,item):
        self.data.append(item)
    def remove(self):
        self.data.pop()
    def top(self):
        return self.data[-1]
stack =Stack()
print(stack)