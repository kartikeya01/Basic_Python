# Name: Kartikeya Sharma
# Session: Afternoon
import math

# Question 1
# Expected output at input = 13:
# 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1
def CollatzConjecture(input):

    if input <= 0:
        print("ERROR - Input has to be greater than 0")
        return

    print(input)

    if input != 1:

        if input % 2 == 0:
            input = int(input / 2)

        elif input % 2 == 1:
            input = int((3 * input) + 1)

    elif input == 1:
        return

    CollatzConjecture(int(input))

# Question 2

def Question2():

    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))
        print(a/b)
    except ValueError:
        print("ValueError - Input was not an integer")
    except ZeroDivisionError:
        print("ZeroDivisionError - b cannot be negative")

# Question 3
# Expected Output of n = 12
# 2 2 3
def PrimeFactors(n):

    if n == 0:
        print(0)
        return

    if n % 2 == 1:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                print(int(i))
                n = n / i

    if n % 2 == 0:
        while n % 2 == 0:
            print(2)
            n = n / 2

    if n > 2:
        print(int(n))
    if n < 2:
        return


# Question 4
# Input: 7
# Output: 2, 3, 5, 7
def PrimeNumbers(n):

    if n < 1:
        return False

    for n in range(2, n+1):
            for i in range(2,n):
               if (n % i) == 0:
                   break
            else:
               print(n)

#print (CollatzConjecture(7))

# print (Question2())

# print(PrimeFactors(12))

# print(PrimeNumbers(13))

