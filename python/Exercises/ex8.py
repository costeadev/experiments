# 1. Create a list of your favorite foods and print them all
fav_foods = ["Pizza","Mac & Cheese","Lasagna","Deep fried eggplants"]

print("My favorite foods")
print("-----------------")
for food in fav_foods:
    print(food)



# 2. Ask the user 3 numbers, store them in a list, and print the sum

def sum_numbers(array):
    total = 0
    for number in array:
        total += number
    return total

def get_valid_integer(prompt):
    # Makes sure the user input is valid
    while True:
        if (prompt % 2 == 0):
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

array = []
number_count = int(get_valid_integer("\nHow many numbers do you want to add?: "))

for i in range(0,number_count):
    number = int(get_valid_integer(f"Number {i+1}: "))
    array.append(number)

sum = sum_numbers(array)
print(sum)



# 3. Ask names until the user types 'stop', then greet each person

names = []
while (1):
    name = input("\nGimme a name: ")
    if (name.lower() == "stop"):
        for name in names:
            print(f"\nHello {name}!")
        break
    else:
        names.append(name)
