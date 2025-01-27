def bill_splitter():
    total_bill = float(input("Enter the total bill amount: "))
    num_people = int(input("Enter the number of people: "))
    tip_percentage = float(input("Enter the tip percentage: "))
    total_bill += total_bill * tip_percentage / 100
    amount_per_person = total_bill / num_people
    print(f'Each person has to pay: {amount_per_person}')
bill_splitter()
    
    