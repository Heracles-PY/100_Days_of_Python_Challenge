print("Welcome to the tip calculator!")
price = float(input("What was the total bill?"))
tip_amount = int(input("What percentage would you like to tip? 10, 15, or 20?"))

total_bill = price + (price * (tip_amount / 100))

print(f"The total amount owed is: ${total_bill:.2f}")
