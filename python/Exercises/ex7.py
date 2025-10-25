def multiply(num1,num2):
    # Multiplies 2 numbers, returns result
    return num1 * num2



def greet_user(name="Stranger"):
    # Greets user with provided name. Default = 'Stranger'
    print(f"\nHello {name}!")



def calculate_area(length,width):
    # Calculates area of a rectangle
    return length * width

def get_valid_integer(prompt):
    # Makes sure the user input is valid
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")



# Main Program

print("\nMultiply numbers!")
print("----------")
num1 = get_valid_integer("Number 1: ")
num2 = get_valid_integer("Number 2: ")
result = multiply(num1,num2)
print(f"\nResult is {result}")

print("\nGreet user")
print("----------")
name = input("What is your name?: ")
greet_user(name)

print("\nCalculate area of a rectangle")
print("----------")
length = get_valid_integer("Length: ")
width = get_valid_integer("Width: ")
area = calculate_area(length,width)
print(f"\nArea is {area}")


