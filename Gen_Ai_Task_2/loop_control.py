daily = [200, 150, 0, 400, 50, -1, 300]
total_sales = 0

for sales in daily:
    if sales == -1:
        print("Corrupted data found")
        break
    elif sales == 0:
        print("No sales today")
        continue
    print(sales)
    total_sales += sales
print(f"Total Sales: {total_sales}")