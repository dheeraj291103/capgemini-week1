n=int(input("Enter a number:"))
def factorial(n):
    if n<0:
        return "Factorial is not possible for negative numbers"
    elif n==0:
        return 1
    else:
        return n*factorial(n-1)
result=factorial(n)
print(f'The factorial of {n} is {result}')
 
    