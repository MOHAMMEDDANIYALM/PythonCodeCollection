n = int(input(" ENTER A NUMBER :"))

# TO CHECK PRIME 

def is_prime(num):
    if num < 2 :
        return False
    for i in range (2,int(num**0.5)+1):
        if num % i == 0:
            return False 
    return True
if is_prime(n):
    print ("IT IS A PRIME NUMBER")
else:
    print ("IT IS NOT A PRIME NUMBER")
 
 # TO CHECK ODD OR EVEN 

def is_even(num): 
    if n % 2 == 0:
        return False
    if n % 2 != 0: 
        return False
    return True
if is_even(n):
    print ("IT IS A EVEN NUMBER")
else : 
    print ("IT IS A ODD NUMBER")

# TO CHECK THE FACTORIAL NUMBER

def factorial(n):
    if n == 0 or n == 1:
        return 1 
    return n * factorial(n-1)
print (f"factorial of {n} is {factorial(n)}")

# SUM THE DIGITS 
a = int(input("ENTER FIRST LETTER TO SUM:"))
b = int(input("ENTER SECOND LETTER TO SUM:"))
def add_numbers(x,y):
    return x + y
print ("sum is:",add_numbers(a, b))