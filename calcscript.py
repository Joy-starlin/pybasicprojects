#clean calculator script
x=float(input("Enter your first number: "))
y=float(input("Enter your second number: "))
z=input("Choose your operation (+, -, *, /, %): ")
if z=='+':
    result=x+y
elif z=='-':
    result= x-y
elif z=='*':
    result= x*y
elif z=='/':
    result= x/y
elif z=='%':
    result= x%y
print(result)