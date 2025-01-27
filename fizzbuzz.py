n=0
while True:
    n+=1
    if n==101:
        break
    if(n%3==0):
        print("Fizz")
    elif(n%5==0):
        print("Buzz")
    elif(n%3==0 and n%5==0):
        print("FizzBuzz")
    else:
        print(n)