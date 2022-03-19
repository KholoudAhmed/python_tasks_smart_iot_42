str = "hello from the dark side  "
index = 'i'
count =0
for iterator in range(len(str)):
    if str[iterator] == index:
        count = iterator+1

print(count)