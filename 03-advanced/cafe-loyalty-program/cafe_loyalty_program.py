def add_purchase():
    name = input('Input Customer Name ')
    try:
        amount = float(input('Enter Purchase Amount : '))
        points = int(amount)  # 1 point per $1
        customers[name] = customers.get(name, 0) + points
        print(f'{name} now has {customers[name]} points')
    except:
        print('Invalid Amount')


def redeem_points():
    global total_free_coffees  # ✅ Needed because we are modifying the global variable
    name = input('Input Customer Name ')
    if name in customers:
        if customers[name] >= 50:
            customers[name] = customers[name] - 50
            total_free_coffees = total_free_coffees + 1
            print(f'{name} redeemed a coffee!')
        else:
            print('Not enough points')
    else:
        print('Customer not found!')


def show_points():
    name = input('Input Customer Name ')
    print(f'{name} has {customers.get(name, 0)} points')


def show_summary():
    print(f'\nCafe: {cafe_name} - {cafe_location}')
    print(f'Total free coffees : {total_free_coffees}')


# Fixed café details
cafe_name = 'JavaBeans Coffee'
cafe_location = 'Colombo'

customers = {}
total_free_coffees = 0

while True:
    print("\n1. Add Purchase")
    print("2. Redeem Free Coffee")
    print("3. Show Points")
    print("4. Show Summary")
    print("5. Exit")
    
    choice = input('Input Choice ')
    
    if choice == '1':
        add_purchase()
    elif choice == '2':
        redeem_points()
    elif choice == '3':
        show_points()
    elif choice == '4':
        show_summary()
    elif choice == '5':
        break
    else:
        print('Invalid Choice!')
