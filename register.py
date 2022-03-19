from fileHandler import insertData

import re
emailRegex =  r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
phoneRegex = r'^01[0125][0-9]{8}$'
def validateName(varName):
    attr = input("plz enter your name: ")
    if attr.isalpha():
        return attr

    return validateName(varName)

def validateMail(varMail):
    attrMail = input("plz enter your mail: ")
    if attrMail:
        if re.fullmatch(emailRegex,attrMail):
            return attrMail

    return validateMail(varMail)

def validatePhone(varPhone):
    attrPhone = input("plz enter your phone: ")
    if attrPhone:
        if re.fullmatch(phoneRegex,attrPhone):
            return attrPhone

    return validatePhone(varPhone)

def validatePassword(varPassword):
    varPassword = input("plz enter your password")
    SpecialSym = ['$', '@', '#', '%']
    flag = True
    if len(varPassword)<6:
        print("length should be at least 6")
        flag = False
    if len(varPassword)>20:
        print("length should be not be greater than 8")
        flag = False
    if not any(char.isdigit() for char in varPassword):
        print('Password should have at least one numeral')
        flag = False
    if not any(char.isupper() for char in varPassword):
        print("Password should have at least one uppercase letter")
        flag = False
    if not any(char.islower() for char in varPassword):
        print("Password should have at least one lowercase letter")
        flag = False
    if not any(char in SpecialSym for char in varPassword):
        print("Password should have at least one of the symbols $@#")
        flag = False
    if flag == True:
        return varPassword
    return validatePassword(varPassword)

def readPassword():
    password = validatePassword("password")
    re_password = validatePassword("re-password")
    if password == re_password:
        return password
    else:
        return readPassword()


# ***********************************Register Funtion********************************************************
def register():
    print("--------hello from register---------")
    fname = validateName("fname")
    lname = validateName("lname")
    password = readPassword()
    email = validateMail("e-mail")
    phone = validatePhone("phone")
    info = [email,password,fname,lname,phone]
    users_info = ":".join(info)
    insertData(users_info)
# ************************************************************************************************************