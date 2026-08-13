prices = [100, 250, 400, 1200, 50, 2000, 850]

expensive_prices = list(filter(lambda price : price >500, prices))
affordable_prices = list(filter(lambda price : price <= 500, prices))


print(expensive_prices)
print(affordable_prices)