foods=[]
prices=[]
total=0

while True:
    food = input("Enter food item (or 'done' to finish): ")
    if food.lower()== "done":
        break
    else:
        price = float(input(f"Enter price for {food}: ₹"))
        foods.append(food)
        prices.append(price)

print("\n----------Shopping Cart Summary ----------")
print(f"{'Item':<20} {'Price (₹)':>10}")
print("-" * 30)

for i in range(len(foods)):
    print(f"{foods[i]:<20} {prices[i]:>10.2f}")
    total += prices[i]

print("-" * 30)
print(f"{'Total':<20} ₹{total:>10.2f}")
print(f"Your total is: ₹{total:.2f}")    
print("Thank you for shopping with us!")
print("Have a great day!")
