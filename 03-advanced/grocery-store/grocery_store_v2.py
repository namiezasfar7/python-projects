#Calculation function
def calculation():
		
	#Calculate bill amount
	bill_amount = 0
	for i in range(4):
		enter_product_type = product_type[i]
		quantity = product_quantity[i]
		price = product_prices[enter_product_type]
		bill_amount = bill_amount + (price * quantity)
	
	#Calculate discount amount
	if bill_amount > 5000:
		discount_amount = bill_amount * 0.1
	else:
		discount_amount = 0
	
	final_amount = bill_amount - discount_amount
	
	return bill_amount, discount_amount, final_amount

#Product Type & Their Prices
product_prices = {
	'rice' : 250,
	'sugar' : 200,
	'milk' : 150,
	'eggs' : 50
}

#Input Customer Name
print('Welcome to the Grocery Shop')

customer_name = input('Input Customer Name ')

#Product type and quantity saver
product_type = []
product_quantity = []

#Product type & quantity iteration
for i in range(4):
	enter_product_type = str(input('Input Product Type (Rice, Sugar, Milk, Eggs) ')).lower()
	enter_product_quantity = int(input('Input Product Quantity '))
	
	product_type.append(enter_product_type)
	product_quantity.append(enter_product_quantity)

#Call back relevant amounts
bill_amount, discount_amount, final_amount = calculation()

#Print Final
print('\n------RECIEPT------')
print('\nCustomer Name : ', customer_name)
print('Products : ', product_type)
print('Product Quantities : ', product_quantity)

print('\n--------------------')
print('Bill Amount : ', bill_amount)
print('Discount Amount : ', discount_amount)
print('Final Amount : ', final_amount)