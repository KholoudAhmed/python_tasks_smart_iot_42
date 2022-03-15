num=int(input('Enter a number: '))

def fizzbuzz(num):

    if num % 3 == 0:

        return 'Fizz'

    elif num % 5 == 0:

        return 'Buzz'

    elif num % 15 == 0:

        return 'Fizzbuzz'

    else:
        return "invalid"

        return num

print(fizzbuzz(num))

