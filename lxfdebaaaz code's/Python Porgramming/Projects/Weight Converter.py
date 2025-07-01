weight=float(input("Enter your weight: "))
unit=input("enter the unit (K/L): ")
if unit == "k" or unit == "K" or unit == "l" or unit == "L":
    print(f"The weight you entered is: {weight}{unit}")
    if unit=="k" or unit=="K":
        weight = weight*2.205
        unit="Lbs."
        print(f"The weight is {round(weight,2)}{unit}")
    else:
        weight = weight/2.205
        unit="Kgs."
        print(f"The weight is {round(weight,2)}{unit}")
else:
    print(f"Error: Invlid unit {unit}. Please use 'k' for Kg or 'l' for Lbs")
