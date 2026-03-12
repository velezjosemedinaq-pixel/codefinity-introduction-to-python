product_type = "Perishable"
days_until_expiration = 3
stock_level = 100
if product_type == "Perishable":
    if days_until_expiration <= 3 and stock_level > 50:
        print("30% discount applied")
    elif 4 <= days_until_expiration <= 6 and stock_level > 50:
        print("20% discount applied")
    elif days_until_expiration > 6 or  stock_level <
        