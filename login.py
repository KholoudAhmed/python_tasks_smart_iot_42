from fileHandler import checkUsers
from ProjectMenu import *

def login():
    print("-----------hello from login------------")
    mail = input("plz enter your email")
    password = input("plz enter your password")
    print("before the if")
    if checkUsers(mail,password):
        print("logged in successfully")
        projectMenu(mail)

