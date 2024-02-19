file = open("youtube.txt", "w")

try:  # This is the first way to handle the error in python 
    file.write("Chai and code")
finally:
    file.close()


# This is the second way to handle the error in python
