print("plz enter ths string")
str = input()
str1 = ""
vowels = ['a','e','i','o','u']
for iterator in range(len(str)):
    if str[iterator] not in vowels:
        str1=str1+str[iterator]

str = str1
print(str1)