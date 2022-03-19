from projectHandler import  *

# ******************************************Project Menu Function ***********************************************
def projectMenu(mail):
    attr = input("plz enter A for Add_project and V for View_project and E for Edit_project and D for Delete_project")
    if attr == "A" or attr == "V" or attr == "E" or attr == "D":
        if attr == "A":
            addProject(mail)

        elif attr == "V":
            viewProject(mail)

        elif attr == "E":
            editProject(mail)

        elif attr == "D":
            deleteProject(mail)

        else:
            print("invlid option")

    projectMenu(mail)

# ****************************************************************************************************************