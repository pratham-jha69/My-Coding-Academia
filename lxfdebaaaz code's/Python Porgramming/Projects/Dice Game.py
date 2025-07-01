# ● ┌ ─ ┐ │ └ ┘
import random
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│    ●    │",
        "│         │",
        "│    ●    │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│    ●    │",
        "│    ●    │",
        "│    ●    │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("How many dice do you want to roll?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
print(dice)

# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)
#     print()

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end=" ")
    print()

# for die in dice:
#     for line in range(5):
#         print(dice_art.get(die)[line])
#     print()

for die in dice:
    total+=die
print(f"Total: {total}")