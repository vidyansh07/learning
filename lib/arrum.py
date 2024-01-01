data = 0


def max(userInput):
    max = 0
    for data in userInput:
        print(data)
        if max < data:
            max = data

    return max


def min(userInput):
    small = 0
    for data in userInput:
        print(data)
        if small > data:
            small = data
    return small
