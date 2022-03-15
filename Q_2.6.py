def arrangFun():
    l = []
    totalSum = 0
    count = 0
    avg = 0.0
    while True:
        num = input("plz enter the numbers you want to calc : ")
        if not num.isalpha():
            if num == "done":
                for iterator in l:
                    totalSum = totalSum + int(iterator)

                count = len(l)
                avg = totalSum/count
                print("the count is :", count)
                print("the total is : ", totalSum)
                print("the average is : ", avg)
                break

            else:
                print("please enter the valid data")

        else:
            l.append(num)


arrangFun()
