items = {
	'apple' : 100,
	'milk' : 200,
	'bread' : 150
}

bucket = []

for i in range(3):
	item = input('Input Item (Apple, Milk, Bread) ').lower()
	quantity = int(input('Input Quantity '))
	
	bucket.append((item, quantity))

bill_amount = 0
for i in range(3):
	item_name = bucket[i][0]
	quantities = bucket[i][1]
	price = items[item_name]
	bill_amount = bill_amount + (price * quantities)

print('\n===BILL===')
print('All Items : ', bucket)
print('Bill Amount : ', bill_amount)
if bill_amount > 1000:
	print('You earned a 5% discount!')