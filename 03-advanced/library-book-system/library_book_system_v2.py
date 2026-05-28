def add_record():
	try:
		name = input('Input Name ')
		book_title = input('Input Book Title ')
		days_late = int(input('Input Days '))

		if name == '' or book_title == '':
			raise ValueError('Empty name or title not allowed')
	
		if book_title in record:
			print('Book already in record!')
			# Changing Fixed Record Not Allowed!
		else:
			record[book_title] = (name, days_late)
			print('Record added successfully!')
	
	except ValueError as e:
		print('Invalid Input:', e)
	
	except:
		print('Unexpected Error!')

def calculate_fine():
	book = input('Input Book Title ').strip()
	if book in record:
		name, days_late = record[book]
		fine = days_late * 0.25
		print(f'Fine for {name} is $ {fine:.2f}')
	else:
		print('Book not found')

def show_books():
	print('\n===ALL LATE RETURN BOOKS===')
	for book, (member, days) in record.items():
		print(f'{book} > {member}, {days} days late')

record = {}

while True:
	print('\n1. Add new record')
	print('2. Calculate Fine')
	print('3. Show all late books')
	print('4. Exit')
	
	choice = input('Input Choice ')
	
	if choice == '1':
		add_record()
	
	elif choice == '2':
		calculate_fine()
	
	elif choice == '3':
		show_books()
	
	elif choice == '4':
		break
	
	else:
		print('Invalid choice!')