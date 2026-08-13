n = int(input("Enter Number : "))

def factorial(n):
    if n < 0:
        return "Enter Positive Number"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(n))
