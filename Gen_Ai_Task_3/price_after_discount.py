
product_price = int(input("Enter Product Price : "))
discount_percentage = int(input("Enter the Dicount percentage : "))


def apply_discount(product_price, discount_percentage=5 ):
    final_discountamount = 0
    if discount_percentage <= 60:
        discount_amount = product_price * discount_percentage / 100
        final_discountamount = product_price - discount_amount
        return final_discountamount
    else:
         discount_amount = product_price * 60 / 100
         final_discountamount = product_price - discount_amount
         return final_discountamount

print(apply_discount(product_price, discount_percentage))