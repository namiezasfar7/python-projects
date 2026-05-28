def calculation():
    bill_amount = 0
    for i in range(len(seat_type)):
        price = prices[seat_type[i]]
        quantity = seat_quantity[i]
        bill_amount = bill_amount + (price * quantity)
    
    # Discount calculation
    if bill_amount > 5000:
        discount_amount = bill_amount * 0.10
    else:
        discount_amount = 0
    
    final_amount = bill_amount - discount_amount
    return bill_amount, discount_amount, final_amount


# Input Section
customer_name = input('Input Customer Name: ')
number_of_seats = int(input('Input Number of Seat Types (1 to 3): '))

prices = {
    'gold': 1200,
    'silver': 800,
    'bronze': 500
}

seat_type = []
seat_quantity = []

for i in range(number_of_seats):
    enter_seat_type = input('Enter Seat Type (Gold, Silver, Bronze): ').lower()
    enter_seat_quantity = int(input('Input Seat Quantity: '))
    
    seat_type.append(enter_seat_type)
    seat_quantity.append(enter_seat_quantity)

# Calculation
bill_amount, discount_amount, final_amount = calculation()

# Output Section
print('\n===== RECEIPT =====')
print('Customer Name:', customer_name)
print('Seat Types:', seat_type)
print('Seat Quantities:', seat_quantity)
print('\nBill Amount:', bill_amount)
print('Discount Amount:', discount_amount)
print('Final Amount:', final_amount)
