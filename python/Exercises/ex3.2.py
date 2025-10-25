# MULTIPLICATION TABLE GENERATOR

number = int(input("Input a number: ")) # Asks user for input

# Anti mutliplicate por 0 line
if number == 0:
    print("Bobo o que?")
    exit()
    
# Multiplication generator
for i in range(1,11):
    print(f"{number} x {i} = {number * i} ")
