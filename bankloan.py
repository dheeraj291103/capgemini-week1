def bankloan(age, income,credit_score):
    if age>=18 and income>=25000 and credit_score>=700:
        print("You are eligible for loan")
    else:
        print("You are not eligible for loan")
age=int(input("Enter your age:"))
income=int(input("Enter your income:"))
credit_score=int(input("Enter your credit score:"))
bankloan(age, income, credit_score)