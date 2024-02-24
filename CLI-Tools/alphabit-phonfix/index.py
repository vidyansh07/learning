def Find(alpha):
    if alpha == 'a':
        return ' for apple'
    elif alpha == 'b':
        return ' for boll'
    elif alpha == 'c':
        return ' for cat'
    elif alpha == 'd':
        return ' for doll'
    elif alpha == 'e':
        return ' for elephant'
    elif alpha == 'f':
        return ' for fan'
    elif alpha == 'g':
        return ' for gun'
    elif alpha == 'h':
        return ' for hen'
    elif alpha == 'i':
        return ' for icecream'
    elif alpha == 'j':
        return ' for jocker'
    elif alpha == 'k':
        return ' for kite'
    elif alpha == 'l':
        return ' for lion'
    elif alpha == 'm':
        return ' for mango'
    elif alpha == 'n':
        return ' for next'
    elif alpha == 'o':
        return ' for orange'
    elif alpha == 'p':
        return ' for parrot'
    elif alpha == 'q':
        return ' for queen'
    elif alpha == 'r':
        return ' for rabbit'
    elif alpha == 's':
        return ' for sun'
    elif alpha == 't':
        return ' for toy'
    elif alpha == 'u':
        return ' for umbralla'
    elif alpha == 'v':
        return ' for van'
    elif alpha == 'w':
        return ' for wall'
    elif alpha == 'x':
        return ' for x-man'
    elif alpha == 'y':
        return ' for yalk'
    elif alpha == 'z':
        return ' for zebra'
    else:
        return "Invalid charecter"


def App():
    print(' Alphabit Phonfix')
    alpha = input("Enter the alphabet\n").lower()
    result = Find(alpha)
    print(alpha, result)


App()
