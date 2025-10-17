num1=float(input("Enter the number 1"))
num2=int(input ("Enter the number2"))

sum=num1+num2
sub=num1-num2
divison=num1/num2

operation=input("Enter the sign")

if operation == "+":
    print(sum)
elif operation == "-":
    print(sub)
elif operation == "/":
    print(divison)
else:
    print("the operation could not be executed")

