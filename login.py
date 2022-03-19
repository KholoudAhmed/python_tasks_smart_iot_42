from ProjectMenu import *

# ******************************** Login Function ****************************************************************
def login():
    print("-----------hello from login------------")
    mail = input("plz enter your email: ")
    password = input("plz enter your password: ")
    if checkUsers(mail,password):
        print("logged in successfully")
        projectMenu(mail)
# ******************************************************************************************************************

