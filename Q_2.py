# listOfNumbers = [1,5,98,76,54]
# #print(listOfNumbers.sort(reverse=True))
# print(listOfNumbers)
# listOfNumbers.sort()
# print(listOfNumbers)
# listOfNumbers.sort(reverse=True)
# print(listOfNumbers)

str = []
print("plz enter the 5 elements of array")
for iterator in range(5):
    num = input()
    if num.isnumeric():
        print("plz enter the value")

    else:
        str.append(num)

str.sort(reverse=True)
print(str)
