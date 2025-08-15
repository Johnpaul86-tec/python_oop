def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price
    
price = float(input("Enter the original price: "))
discount_input = input("Enter the discount percentage (e.g., 5 or 5%): ")
discount = float(discount_input.replace('%', '').strip())


final_price = calculate_discount(price, discount)

if discount >= 20:
    print(f"Discount applied. Final price: {final_price}")
else:
    print(f"No discount applied. Final price: {final_price}")
