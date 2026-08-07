try:
    order_amount = int(input("Enter Order Amount: "))
except ValueError:
    print("Please Enter Valid Amount")
    raise SystemExit

discount = 0


if order_amount >= 2000:
    discount = 15
elif order_amount >= 1500:
    discount = 10
elif  order_amount >= 1000:
    discount = 7
else:
    discount = 0

discount_amount = order_amount * discount / 100
final_amount = order_amount - discount_amount

tax = 5
tax_amount = final_amount * tax / 100
final_payable = final_amount + tax_amount

print(f"Order Amount: {order_amount}")
print(f"Discount: {discount}%")
print(f"Discount Amount: {discount_amount}")
print(f"Final Amount: {final_amount}")
print(f"Tax : {tax}")
print(f"Taxable Amount: {tax_amount}")
print(f"Final Payable: {final_payable}")