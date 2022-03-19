print("plz enter the number")
num = int(input())
s = 2 * num - 2
for iterator in range(0, num):
    for j in range(0, s):
        print(end=" ")
    s = s - 2
    for j in range(0, iterator + 1):
        print("* ", end="")
    print("\n")