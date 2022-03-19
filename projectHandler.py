from fileHandler import *
from projectValidation import *
from datetime import datetime

# *******************insert data in project*********************************************************************
def insertProjectData(info):
    with open("projects.txt","a") as afile:
        data = info.strip("\n")
        data = f"{data}\n"
        afile.write(data)
        afile.close()
# **************************************************************************************************************
# **********************************add project******************************************************************
#                                 1-projectid
#                                 2-project Details
#                                 3-project title
#                                 4-startDate
#                                 5-endDate
def addProject(mail):
    print("-----------hello from adding function-----------")
    projectId = input("plz enter your project id: ")
    while True:
        if projectId.isnumeric():
            if checkUinqueProjectId(projectId):
                break
        else:
            projectId = input("plz enter a valid project id")

    projectTitle = validateProjectTitle("projecttile")
    projectDetails = validateProjectDetails("projectDetails")
    projectTarget = validateProjectTarget("projectTarget")
    startDate = input("plz enter the start Date in this format yyyy-mm-dd" )
    dateFormat = "%Y-%m-%d"
    while True:
        if startDate:
            firstDate=datetime.strptime(startDate,dateFormat)
            break
        else:
            startDate=input("plz enter a valid first date")

    endDate = input("plz enter the end Date in this format yyyy-mm-dd")
    dateFormat = "%Y-%m-%d"
    while True:
        if startDate:
            finalDate=datetime.strptime(endDate,dateFormat)
            break
        else:
            endDate=input("plz enter a valid final date")
            break

    info = [mail,projectId,projectTitle,projectTarget,projectDetails,startDate,endDate]
    project_info = ":".join(info)
    insertProjectData(project_info)
# ***************************************************************************************************************
# *********************************View Project Function**********************************************************
def viewProject(mail):
    print("-------------------hello from viewing function--------------")
    print("----------------------- ALL PROJECTS -----------------------")
    with open("projects.txt", 'r') as pfile:
        projects = pfile.readlines()
        for project in projects:
            project_info = project.split(":")
            print(project_info)
    return True
# *****************************************************************************************************************
# *******************************Edit Project Funtion************************************************************
def editProject(mail):
    print("----------------hello from editing function------------------")
    allProjects=[]
    with open("projects.txt",'r') as rfile:
        projects=rfile.readlines()
        for project in projects:
            project=project.strip("\n")
            project_info=project.split(":")
            allProjects.append(project_info)
            if project_info[0]==mail:
                print(project_info)
#** *************************************************************************************************************
    projectId=input("plz enter the project id: ")
    if projectId.isnumeric():
        flag = False
        projectId=int(projectId)
        print(allProjects)
        for i in allProjects:
            print(i)
            if int(i[1])== int(projectId):
                print(i)
                attr=input("plz select your choice:\n"
                           "'1' Edit project titlt:\n"
                           "'2' Edit project details:\n"
                           "'3' Edit project target:\n"
                           "'4' Edit project start date:\n"
                           "'5' Edit project end date :")
                if attr=='1':
                    arg=input("plz enter new title: ")
                    while True:
                        if arg.isalpha():
                            i[2]=arg
                            flag=True
                            with open("projects.txt",'w') as wfile:
                                for all in allProjects:
                                    all = ":".join(all)
                                    wfile.write(all)
                                    wfile.write("\n")
                            break
                        else:
                            arg=print("invalid data please enter an new title")
                if attr=='2':
                    arg=input("plz enter new details: ")
                    while True:
                        if arg.isalpha():
                            i[3]=arg
                            flag=True
                            with open("projects.txt",'w') as wfile:
                                for all in allProjects:
                                    all = ":".join(all)
                                    wfile.write(all)
                                    wfile.write("\n")
                            break
                        else:
                            arg=print("invalid data please enter an new details")
                if attr=='3':
                    arg=input("plz enter new target: ")
                    while True:
                        if arg:
                            i[4]=arg
                            flag=True
                            with open("projects.txt",'w') as wfile:
                                for all in allProjects:
                                    all = ":".join(all)
                                    wfile.write(all)
                                    wfile.write("\n")
                            break
                        else:
                            arg=print("invalid data please enter an new title")

                    if flag==True:
                        break
        else:
            project=input("plz enter your correct project id")
        return  True

# ***************************************************************************************************************
# ************************Delete Project Function***************************************************************
def deleteProject(mail):
    print("---------- hello from deleting function ---------------")
    print("Here's a list of all your projects:\n")
    allProjects = []
    with open("projects.txt", 'r') as pfile:
        projects = pfile.readlines()
        for project in projects:
            project_info = project.split(":")
            allProjects.append(project_info)
            if project_info[0] == mail:
                print(project_info)

    projectId = input("enter id of project you want to delete: ")
    if projectId.isnumeric():
        # print(allProjects)
        for pos, project in enumerate(allProjects):
            # print(project)
            print(projectId,project[1])
            if int(project[1]) == int(projectId):
                # allProjects[pos].clear()
                if mail==project[0]:
                    del allProjects[pos]
                    print(allProjects)
                else:
                    print("you tried to access email doesn't belong to you :(")

        with open("projects.txt", 'w') as pfile:
            # with open("projects.txt", "a") as pfile:
            for project in allProjects:
                pfile.write(":".join(project))

    else:
        myProject=input("invalid option ,plx enter the new data")

    return True
# ****************************************************************************************************************