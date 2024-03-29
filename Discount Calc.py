def calculate_discount(price,discount_percent):
  
  Discount_Amount= 0
  if discount_percent >= 20 :
    Discount_Amount = price * (discount_percent/100)
    price = price - Discount_Amount
    print("Final price of product is K", price)
  else:
    price = price + 0
    print("Final price of product is K", price)

print("WELCOME TO DISCOUNT CALCULATOR. ")

user_price =  int(input("Enter price of product: K"))
user_discount_percent =  float(input("Enter discont percent on product: "))

calculate_discount(user_price,user_discount_percent)
#print(" Final price of product is K", user_price)