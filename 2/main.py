print("Welcome toe the tip calculator.")
price = float(input("What was the total bill? $"))
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
how_many = int(input("How many people to split the bill? "))
price_with_tip = price * (1 + percentage / 100)
price_per_person = "{:.2f}".format(price_with_tip / how_many, 2)
print(f"Each person should pay: ${price_per_person}")
