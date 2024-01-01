from time import sleep


def App():
    inter_time = int(input("Enter the countdown time: \n"))
    for start in range(inter_time, -1, -1):
        print(start)
        sleep(1)


App()
