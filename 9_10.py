cart_total = 120
is_member = True
has_coupon = False

is_member_and_cart_over_100 = is_member and (cart_total > 100)
is_member_and_cart_over_50 = is_member and (cart_total > 50)
is_member_and_cart_less_50 = is_member and (cart_total < 50)

has_coupon_and_cart_over_100 = has_coupon and (cart_total > 100)
has_coupon_and_cart_over_50 = has_coupon and (cart_total > 50)
has_coupon_and_cart_less_50 = has_coupon and (cart_total < 50)
if is_member_and_cart_over_100:
    print("Member discount: 20% off + free shipping")
if is_member_and_cart_over_50:
    print("member discount: 10% off + free shipping")
if is_member_and_cart_less_50:
    print("member discount: 5 off")
if has_coupon_and_cart_over_100:
    print("coupon discount: 10%")
if has_coupon_and_cart_over_50:
    print("coupon discount: 5%")
if  has_coupon_and_cart_less_50:
    print("no discount become a member")

discount_rules = [
    {"condition":lambda: is_member and cart_total > 100, "message":lambda: "member dicount:20% off +free shipping"},
    {"condition":lambda: is_member and cart_total > 50, "message":lambda: "member dicount:10% off +free shipping"},
    {"condition":lambda: is_member and cart_total < 50, "message":lambda: "member dicount:5% off"},
    {"condition":lambda: not is_member and has_coupon, "message":lambda: "coupon discount: 10"},
    {"condition":lambda: not is_member and cart_total > 100, "message":lambda: "discount 5%"},
    {"condition":lambda: not is_member and cart_total < 100, "message":lambda: "no discount become a member"} 
]

for rule in discount_rules:
    if rule["condition"]():
        print(rule["message"])
        break