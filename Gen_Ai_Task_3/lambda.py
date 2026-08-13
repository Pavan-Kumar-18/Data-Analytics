price = int(input("Enter Price: "))
gst = lambda : price + (price * 18) / 100
print(gst())