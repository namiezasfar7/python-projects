def summarize_expense(expenses):
	category_totals = {}
	
	for category, amount in expenses:
		if category in category_totals:
			category_totals[category] = category_totals[category] + amount
		else:
			category_totals[category] = amount
	
	highest_category = None
	highest_amount = 0
	
	for category, total in category_total.items():
		if total > highest_amount:
			highest_amount = total
			highest_category = category
	
	grand_total = sum(category_totals.values())
	
	return catergory_totals, highest_category, highest_amount, grand_total

expenses = []

while True:
	category = str(input('Enter Category or Exit to exit'))
	
	if catergory.lower == 'exit':
		break
	
	amount = float(input('Input Expense for Category '))
	
	expenses.append((category,amount))

catergory_totals, highest_category, highest_amount, grand_total = summarize_expense(expenses)

print("\n----- Expense Summary -----")
for category, total in category_totals.items():
	print(f'{category : < 10}: LKR {total : .2f}')
	
print(f"\nTotal Expenses: LKR {grand_total:.2f}")
print(f"Highest Spending Category: {highest_category} (LKR {highest_amount:.2f})")

# High spending alert
if grand_total > 10000:
    print("⚠️ High Spending Alert! You've spent over LKR 10,000.")
