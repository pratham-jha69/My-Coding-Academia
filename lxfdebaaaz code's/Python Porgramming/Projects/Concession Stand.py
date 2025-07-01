from collections import Counter  # <--- this line is necessary


menu = {"hot dog": 3.50,
        "hamburger": 4.00,
        "cheeseburger": 4.50,
        "french fries": 2.50,
        "soda": 1.50,
        "water": 1.00}
cart=[]
total=0

print("Welcome to the Concession Stand!")
print("---------MENU---------")

for key, value in menu.items():
    print(f"{key:15}: ${value:.2f}")
print("-----------------------")

while True:
    food = input("Enter an item ('q' to quit): ").lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("Item not on the menu. Please try again.")
print("--------YOUR ORDER--------")
item_count = Counter(cart)
for food,count in item_count.items():
    print(f"{count} x {food:15}: ${menu[food] * count:.2f}")
print("--------------------------")

for food in cart:
    total += menu[food]
print(f"Total: ${total:.2f}")
# print(cart)
# for food in cart:
#     total+=menu[food]
# print(f"Total: ${total:.2f}")