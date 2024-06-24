print("Welcome to the tip calculator!")
bill = int(input("What was the total bill? $"))
tip_percent = int(input("How much would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_amount = bill * tip_percent / 100
total_bill = bill + tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${bill_per_person:.2f}")