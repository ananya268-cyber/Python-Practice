def calculate_product_or_sum(a,b):
    if a*b <=1000:
        return a*b
    else:
        return a+b

a = int(input("enter a number: "))
b = int(input("enter another number: "))   
result = calculate_product_or_sum(a,b)

print(f"The result is: {result}")

