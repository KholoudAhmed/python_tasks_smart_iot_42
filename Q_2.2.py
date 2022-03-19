mulipliList = []

print("plz enter the number of multpli table you want : ")
num = int(input())

for iterator in range(1,num+1):
    listOfList = []
    for index in range(1,iterator+1):
        listOfList.append(iterator*index)
    mulipliList.append(listOfList)

print(mulipliList)
