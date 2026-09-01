print("Welcome to the tip calculator!")
price = input("What was the total bill?")
tip_amount = input("What percentage would you like to tip? 10, 15, or 20?")

total_bill = float(price) + (float(price) * (float(tip_amount) / 100))

print(f"The total amount owed is: ${total_bill:.2f}")
