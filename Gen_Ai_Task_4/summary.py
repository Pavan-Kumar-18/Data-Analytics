file = open("sales_data.txt", "r")

all_lines = file.readlines()
total_sales = 0
average_sales = 0
highest_sales = 0
lowest_sales = float("inf")

for line in all_lines:
    sales = int(line.rstrip("\n"))
    total_sales += sales
    if sales > highest_sales:
        highest_sales = sales
    if sales < lowest_sales:
        lowest_sales = sales

average_sales = total_sales/ len(all_lines)
    

print("Total Sales:",total_sales)
print("Highest Sales:",highest_sales)
print("Lowset Sales:",lowest_sales)
print("Average Sales:", average_sales)
file.close()