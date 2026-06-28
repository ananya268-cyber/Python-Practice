sum = 0
print("This program calculates the sum of even numbers from 2 to n.")
a = int(input("Enter a number: "))

for i in range(2,a+1):
    if i % 2==0:
        sum+=i
    else:
        continue
print(f"The sum of even numbers from 2 to {a} is: {sum}")