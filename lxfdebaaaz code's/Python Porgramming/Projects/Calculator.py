operator=input("enter the operator (+,-,*,/): ")
num1=float(input("enter the first number: ") )
num2=float(input("enter the second number: "))
           
if operator == "+":
    result=num1+num2
    print(round(result,2))
elif operator == "-":
    result=num1-num2
    print(round(result,2))
elif operator == "*":
    result=num1*num2
    print(round(result,2))
elif operator == "/":
    if num2 !=0:
        result=num1/num2
        print(round(result,2))
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operator. Please use +, -, *, or /.")