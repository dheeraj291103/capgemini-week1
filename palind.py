def palindrome_checker():
    while True:
        value = input("Enter a string or number: ")
        if value == value[::-1]:
            print("It is a palindrome")
        else:
            print("It is not a palindrome")
        choice = input("Do you want to check another value? (yes/no): ")
        if choice.lower() == "no":
            break
palindrome_checker()