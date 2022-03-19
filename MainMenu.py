from register import *
from login import *


def mainMenu():
    x = input("plz enter l for login and r for register: ")
    if x == "l" or x == "r":
        if x == "l":
            login()
        else:
            register()

    return mainMenu()

mainMenu()
