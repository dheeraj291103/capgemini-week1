a=float(input('Enter your weight : '))
b=float(input('ENter your height : '))
c=a/(b*b)
if c<18.5:
    print('Underweight')
elif 18.5<c<25:
    print('Normal')
else:
    print('Normal Weight')