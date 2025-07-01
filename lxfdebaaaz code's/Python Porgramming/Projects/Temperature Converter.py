temp=float(input("Enter the temperature: "))
unit=input("is the temperature in Celsius or Fahrenheit? (C/F): ")
if unit == "c" or unit == "C" or unit == "f" or unit == "F":
    print(f"The temperature you entered is: {temp}°{unit}")
    if unit=="c" or unit=="C":
        temp = (temp*9/5) + 32
        unit="F"
        print(f"The temperature in Fahrenheit is: {temp}°{unit}")
    else:
        temp = (temp-32) * 5/9
        unit="C"
        print(f"The temperature in Celsius is: {temp}°{unit}")
else:
    print(f"{unit}:Invalid unit. Please enter C or F")