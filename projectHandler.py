
from projectValidation import *
# from fileHandler import checkUniqueMail
def insertProjectData(info):
    with open("projects.txt","a") as afile:
        data = info.strip("\n")
        data = f"{data}\n"
        afile.write(data)
        afile.close()

def addProject(mail):
    print("-----------hello from adding function-----------")
    projectId = validateProjectId("prijectID")
    projectTitle = validateProjectTitle("projecttile")
    projectDetails = validateProjectDetails("projectDetails")
    projectTarget = validateProjectTarget("projectTarget")
    # date_string = '2017-12-31'
    # date_format = '%Y-%m-%d'
    # try:
    #     date_obj = datetime.datetime.strptime(date_string, date_format)
    # except ValueError:
    #     print("Incorrect data format, should be YYYY-MM-DD")

    info = [mail,projectId,projectTitle,projectTarget,projectDetails]
    project_info = ":".join(info)
    insertProjectData(project_info)
    # print(info)
def viewProject(mail):
    print("-------------------hello from viewing function--------------")
    print("----------------------- ALL PROJECTS -----------------------")
    with open("projects.txt", 'r') as pfile:
        projects = pfile.readlines()
        for project in projects:
            project_info = project.split(":")
            print(project_info)
    return True


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
  # ********************************************************************************
    projectId=input("plz enter the project id")
    if projectId.isnumeric():
        flag = False
        projectId=int(projectId)
        print(allProjects)
        for i in allProjects:
            print(i)
            if int(i[1])== int(projectId):
                print(i)
                attr=input("plz select your choice\n"
                           "'1' Edit project titlt\n"
                           "'2' Edit project details\n"
                           "'3' Edit project target\n"
                           "'4' Edit project start date\n"
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
                        if arg.isalpha():
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