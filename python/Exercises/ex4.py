# MULTIPLICATION TABLE GENERATOR

def print_table(number):

    # Anti-Multiplicatepor0
    if number == 0:
        print("Que haces bro, eres tonto o tus padres te cagaron por el culo?")
        exit()

    # Print table    
    for i in range(1,11):
        print(f"{number} x {i} = {number * i}")


number = int(input("Input a number: "))
print_table(number)