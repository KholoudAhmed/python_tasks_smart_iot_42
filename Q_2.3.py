def reverseStr(str):
    revStr = " "
    index = len(str)-1
    while index >= 0:
        revStr = revStr + str[index]
        index = index -1
    print(revStr)

str = "kholoud"
reverseStr(str)