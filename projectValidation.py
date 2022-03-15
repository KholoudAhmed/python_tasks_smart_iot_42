

def validateProjectId(varId):
    attr = input("plz enter the project ID")
    if attr.isnumeric():
        return attr

    validateProjectId(varId)

def validateProjectTarget(varTarget):
    attr = input("plz enter the project target")
    if attr.isnumeric():
        return attr

    validateProjectTarget(varTarget)


def validateProjectDetails(varDet):
    attr = input("plz enter the project details")
    if isinstance(attr,str):
        return attr

    validateProjectDetails(varDet)


def validateProjectTitle(varTitle):
    attr = input("p;z enter the project title")
    if attr.isalpha():
        return attr

    validateProjectTitle(varTitle)



