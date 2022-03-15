def arrayFun(Length, Start):
    l = []
    l.append(int(Start))
    for iterator in range(1, int(Length)):
        l.append(int(Start) + int(iterator))
    print(l)

Length = input("plz enter the size of array: ")
Start = input("plz enter the start number: ")
arrayFun(Length, Start)
