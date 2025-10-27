try:
    purchase_amount = float(input("Total bill amount : ₹ "))
    customer_type = input("Customer type ( Premium / Regular / New ) : ").strip().upper()
    coupon = input("Do you have a coupon code ( Y / N ) : ").strip().lower()

    if coupon == "y":
        coupon_code = input("Enter your coupon code ( FESTIVE10 / NEWYEARS5 ) : ").strip().upper()
    else:
        coupon_code = None

    loyalty_points = int(input("Previous earned points : "))

    # ---------- Input Validation ----------
    if not (purchase_amount > 0 and customer_type in ['PREMIUM', 'REGULAR', 'NEW'] 
            and coupon in ['y', 'n'] and loyalty_points >= 0):
        print("\n⚠ Invalid Input: Check all values (amount, customer type, coupon, loyalty points).")

    else:
        discount = 0
        applied_discounts = []

        # ---------- Base Discount ----------
        if customer_type == "PREMIUM":
            discount += (purchase_amount * 15) / 100
            applied_discounts.append("Base 15%")
        elif customer_type == "REGULAR":
            discount += (purchase_amount * 10) / 100
            applied_discounts.append("Base 10%")
        elif customer_type == "NEW":
            discount += (purchase_amount * 5) / 100
            applied_discounts.append("Base 5%")

        # ---------- Purchase Slab Discount ----------
        if purchase_amount >= 100000:
            discount += (purchase_amount * 10) / 100
            applied_discounts.append("Extra 10% (High Purchase Bonus)")
        elif purchase_amount >= 50000:
            discount += (purchase_amount * 5) / 100
            applied_discounts.append("Extra 5% (Mid Purchase Bonus)")

        # ---------- Coupon Discount ----------
        if coupon == "y":
            if coupon_code == "FESTIVE10":
                discount += (purchase_amount * 10) / 100
                applied_discounts.append("Coupon 10% (FESTIVE10)")
            elif coupon_code == "NEWYEARS5":
                discount += (purchase_amount * 5) / 100
                applied_discounts.append("Coupon 5% (NEWYEARS5)")
            else:
                applied_discounts.append("Invalid Coupon (No Discount)")

        # ---------- Loyalty Discount ----------
        if loyalty_points >= 100:
            loyalty_discount = (loyalty_points // 100) * 50
            discount += loyalty_discount
            applied_discounts.append(f"Loyalty ₹{loyalty_discount}")

        # ---------- Final Calculation ----------
        final_amount = purchase_amount - discount

        # ---------- Output ----------
        print("\n" + "*" * 45)
        print(f"Customer Type    : {customer_type}")
        print(f"Total Bill       : ₹{purchase_amount:,.2f}")
        print(f"Applied Offers   : {', '.join(applied_discounts)}")
        print(f"Total Discount   : ₹{discount:,.2f}")
        print(f"Final Payable    : ₹{final_amount:,.2f}")
        print("*" * 45)

except ValueError:
    print("⚠ Invalid Input (Expected numeric values for amount or points).")
