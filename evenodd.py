def odd_even_separator():
    numbers = input("Enter a list of numbers separated by a space: ").split(",")
    odd = []
    even = []
    for number in numbers:
        if int(number) % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    print(f"Odd numbers: {odd}")
    print(f"Even numbers: {even}")
odd_even_separator()