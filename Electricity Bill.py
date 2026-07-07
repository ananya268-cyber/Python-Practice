units_consumed = int(input("Enter number of units consumed this month: "))

if units_consumed < 0:
    print("Units consumed cannot be negative")
elif units_consumed <= 100:
    rate_per_unit = 1.50
    bill = units_consumed * rate_per_unit
    print("Total Bill: ₹", bill)
elif units_consumed <= 200:
    rate_per_unit = 2.50
    bill = units_consumed * rate_per_unit
    print("Total Bill: ₹", bill)
elif units_consumed <= 300:
    rate_per_unit = 4.00
    bill = units_consumed * rate_per_unit
    print("Total Bill: ₹", bill)
else:
    rate_per_unit = 5.00
    bill = units_consumed * rate_per_unit
    print("Total Bill: ₹", bill)