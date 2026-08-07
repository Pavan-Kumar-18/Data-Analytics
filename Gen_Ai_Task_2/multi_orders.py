orders = [1200, 2500, 800, 1750, 3000]
discount = 0
discounted_orders = 0
total_revenue = 0
for order in orders:
    if order >= 2000:
        discount = 15
    elif order >= 1500:
        discount = 10
    elif order >= 1000:
        discount = 7
    else:
        discount = 0
    final_orderamount =  order - order * discount / 100 
    print(f"{order} -> {discount}% -> {final_orderamount}")
    total_revenue += final_orderamount
    if discount > 0:
     discounted_orders += 1
print(f"Total Revenue: {total_revenue}")
print(f"Discounted Orders: {discounted_orders}")