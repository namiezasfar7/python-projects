coffee_types = {
	'espresso' : 400,
	'latte' : 350,
	'mocha' : 450
}

enter_coffee_type = input('Enter Coffee Type (Espresso, Latte, Mocha) ').lower()
enter_coffee_quantity = int(input('Input Quantity of Coffee '))

price = coffee_types[enter_coffee_type]
bill_amount = price * enter_coffee_quantity

print('Bill Amount : ', bill_amount)