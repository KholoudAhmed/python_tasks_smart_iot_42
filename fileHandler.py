
# ******************* Insert UserData in his project *************************************************************
def insertData(info):
    with open("users.txt","a") as afile:
        data = info.strip("\n")
        data = f"{data}\n"
        afile.write(data)
        afile.close()
# ***************************************************************************************************************
# ****************** Authontication functions for users **********************************************************
def checkUsers(email,password):
    with open("users.txt") as rfile:
        users = rfile.readlines()
        for user in users:
            user = user.strip("\n")
            user_info = user.split(":")
            if user_info[0] == email and user_info[1] == password:
                return user_info

    return False
# *******************************************************************************************************************
def checkUniqueMail(mail):
    with open("users.txt") as rfile:
        users = rfile.readlines()
        for user in users:
            user = user.strip("\n")
            user_info = user.split(":")
            if user_info[0] == mail:
                print("your email is repeated")
                exit()

    return True
# *******************************************************************************************************************
# ********************************* Authontication for user's projet *************************************************
def checkUinqueProjectId(projectId):
    with open("projects.txt") as pfile:
        projects = pfile.readlines()
        for proj in projects:
            proj_info = proj.split(":")
            if proj_info[1] == projectId:
                print("repeated project id")
                exit()
    return True
# ****************************************************************************************************************
