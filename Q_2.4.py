import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def Validation(name, mail):
    print(f"the username: {name} \n the usermail: {mail}")

while True:
    name = input("plz enter your name:  ")
    if not name:
        name = input("Empty string, plz enter a valid name: ")
    break
mail = input("please enter your mail: ")
if re.fullmatch(regex, mail):
    Validation(name,mail)
else:
    print("Invalid Email")