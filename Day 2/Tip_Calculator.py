print("Welcome to the tip calculator!")
price = float(input("What was the total bill?"))
tip_amount = int(input("What percentage would you like to tip? 10, 15, or 20?"))
num_people = int(input("How many people to split the bill?"))

price_per_person = (price + (price * (tip_amount / 100))) / num_people

print(f"Each person should pay: ${price_per_person:.2f}")
