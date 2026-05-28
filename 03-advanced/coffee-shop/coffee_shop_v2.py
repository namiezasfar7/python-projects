# Calculation Function
def calculation():
    # Calculate Bill Amount
    bill_amount = 0
    for i in range(3):

        quantity = coffee_quantity[i]
        price = coffee_prices[coffee_flavours[i]]
        bill_amount = bill_amount + (price * quantity)

    # Calculate Loyalty Points
    if bill_amount > 5000:   # loyalty only if exceeds 5000
        loyalty_points = int((bill_amount - 5000) / 1000)
    else:
        loyalty_points = 0

    # Calculate Discount
    if bill_amount > 10000:
        discount_amount = bill_amount * 12 / 100
    else:
        discount_amount = 0

    final_amount = bill_amount - discount_amount

    # Return all values
    return bill_amount, loyalty_points, discount_amount, final_amount


# Input customer details & order
customer_mobile_num = int(input('Input Mobile Number: '))

# Coffee Flavour types & their prices
coffee_prices = {
    'A': 500,
    'B': 300,
    'C': 400,
    'D': 200
}

# Lists to store 3 flavours
coffee_flavours = []
coffee_quantity = []

# Coffee Flavour Iteration
for i in range(3):
    enter_coffee_flavour = input('Input Coffee Flavour (A,B,C,D): ').upper()
    enter_coffee_quantity = int(input('Input Coffee Quantity: '))
    coffee_flavours.append(enter_coffee_flavour)
    coffee_quantity.append(enter_coffee_quantity)

# Call the function and unpack returned values
bill_amount, loyalty_points, discount_amount, final_amount = calculation()

# Print the Customer Receipt
print('\n--- Customer Receipt ---')
print(f'Customer Mobile Number: {customer_mobile_num}')
print(f'Coffee Flavours: {coffee_flavours}')
print(f'Coffee Quantities: {coffee_quantity}')
print(f'\nBill Amount: {bill_amount:.2f} LKR')
print(f'Discount Amount: {discount_amount:.2f} LKR')
print(f'Final Amount: {final_amount:.2f} LKR')
print(f'Loyalty Points: {loyalty_points}')
print('-------------------------------')
print('Thank you for visiting our coffee shop!')
