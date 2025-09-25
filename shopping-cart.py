foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to purchase or press 'q' to quit: ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter price of the {food}: R"))
        foods.append(food)
        prices.append(price)

print("\nYour Cart:")
for food in foods:
    print(food)

for price in prices:
    total += price

print(f"\nYour total is: R{total:.2f}")
