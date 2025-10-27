try:
    purchase_amount = float(input("total bill amount : "))
    customer_type = input("Customer type ( Premium / Regular / New ) : ").strip().upper()
    coupon = input("do you have coupon code ( Y / N ) : ").strip().lower()
    if coupon == "y": 
        coupon_code = input("Enter your coupon code ( FESTIVE10 / NEWYEARS5 ) : ").strip().upper() # coupon code will be : FESTIVE10 = 10% DISCOUNT , NEWYEARS5 = 5% DISCOUNT , OTHERWISE = INVALID COUPON
    loyalty_points = int(input("Previous earned points : "))

    if not ( purchase_amount > 0 and customer_type in [ 'PREMIUM', 'REGULAR', 'NEW' ] and coupon in [ 'y', 'n' ] and loyalty_points >= 0 ):
        print("Invalid Input : ya to aapne koi negative value li hai ya pir aapne koi bhi product buy nahi kiya hai ya aapne customer type galat fill kr diya ya pir coupon code galat hoga")
    else:
        discount = 0
        apply_dis = ""
        
        # Customer Types
        if customer_type == "PREMIUM": # base discount = 15 %
            discount = (purchase_amount * 15) / 100
            apply_dis = "Base 15%"
        elif customer_type == "REGULAR": # base discount = 10 %
            discount = (purchase_amount * 10) / 100 
            apply_dis = "Base 10%"
        elif customer_type == "NEW": # base discount = 5 %
            discount = (purchase_amount * 5) / 100
            apply_dis = "Base 5%"
            

        # Purchase amount according
        if 50000 <= purchase_amount < 100000:# extra discount 5 % 
            discount += (purchase_amount * 5) / 100
            apply_dis += " + Extra 5%"
        if purchase_amount >= 100000 : # extra discount 10 % 
            discount += (purchase_amount * 10) / 100
            apply_dis += " + Extra 10%"

        # Discount Coupons
        if coupon == "y":
            if coupon_code == "FESTIVE10": # EXTRA 10% Discount
                discount += (purchase_amount * 10) / 100
                apply_dis += " + Coupon 10% "

            elif coupon_code == "NEWYEARS5": # EXTRA 5% Discount
                discount += (purchase_amount * 10) / 100
                apply_dis += " + Coupon 5% "
                
        # Loyalty Points
        if loyalty_points >= 100:
            loyalty_points = int(loyalty_points / 100)
            discount += loyalty_points * 50
            loyalty_points *= 50
            apply_dis += f" + Loyalty ₹ {loyalty_points}"
            

        final_amount = purchase_amount - discount

        # final output
        print('\n' + '*' * 30)
        print(f"Customer Type : {customer_type}")
        print(f"Applied Offers : {apply_dis}")
        print(f"Total Discount : ₹ {discount}")
        print(f"Final Amount : ₹ {final_amount}")
        print('*' * 30)

except ValueError:
    print("Invalid Input")