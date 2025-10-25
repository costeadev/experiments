
def factorial(n):
    if n < 0:
        print("Can't print negative numbers, you dork >:(")
        return None

    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result


# User Menu
n = int(input("Input a number: "))
result = factorial(n)

if result is not None:
    print(f"Factorial of {n} is {result}")
