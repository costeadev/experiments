# Fizz Buzz

def fizz_buzz(n):
    if (n % 3 == 0 and n % 5 == 0):
        return("Fizz Buzz")
    elif (n % 3 == 0):
        return("Fizz")
    elif (n % 5 == 0):
        return("Buzz")
    else:
        return(n)
    
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
    
for n in range(start,end+1):
    print(fizz_buzz(n))
              