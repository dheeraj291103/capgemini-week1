import re
def password_strength(password):
    if len(password) < 8:
        return "Password is weak"
    elif re.search('[0-9]',password) is None:
        return "Password is weak"
    elif re.search('[A-Z]',password) is None:
        return "Password is weak"
    elif re.search('[a-z]',password) is None:
        return "Password is weak"
    elif re.search('[!@#$%^&*()_+]',password) is None:
        return "Password is weak"
    else:
        return "Password is strong"
def main():
    password = input("Enter a password: ")
    print(password_strength(password))
if __name__ == "__main__":
    main()