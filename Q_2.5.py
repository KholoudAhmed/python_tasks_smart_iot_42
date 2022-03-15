str = "abdulrahman"
def longest_alphapet(str):
    continueStr = ""
    appendStr = ""
    for character in str:
        if appendStr == "":
            appendStr = character
        elif appendStr[-1] <= character:
            appendStr = appendStr + character
        elif appendStr[-1]>character:
            if len(continueStr) < len(appendStr):
                continueStr = appendStr
                appendStr = character
            else:
                appendStr=character

    if (len(appendStr) > len(continueStr)):
        continueStr = appendStr
    print(continueStr)

longest_alphapet(str)



