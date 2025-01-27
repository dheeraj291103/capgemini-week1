def multiplication_table():
    num=int(input("Enter a number:"))
    start=int(input("Enter the start of the range:"))
    end=int(input("Enter the end of the range:"))
    for i in range(start,end+1):
        print(f'{num} * {i} = {num*i}')
multiplication_table()
