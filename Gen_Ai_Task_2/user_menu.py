orders = []

add_item = True
while True:
    print('\n 1. Add Order')
    print("\n 2. show All Order and Total")
    print("\n q. Quit the Application")
    user_input = input("Enter Choice : ")
    if(user_input == "1"):
         try:
            order_amount = int(input("Enter Order Amount: "))  
         except ValueError:
                print("Please Enter Valid input")
                continue
         orders.append(order_amount)
    elif(user_input == "2"):
        total_revenue = 0
        for order in orders:
            discount = 0
            if order >= 2000:
                discount = 15
            elif order >= 1500:
                discount = 10
            elif order >= 1000:
                discount = 7
            discountAmount = order * discount / 100
            finally_price = order - discountAmount
            print(f"{order} -> {discount}% -> {finally_price}")
            total_revenue += finally_price
        print(f"Total Revenue: {total_revenue}")
    elif(user_input == "q"):
        print("Thank You")
        break
    else:
        print("Invalid choice")
        continue