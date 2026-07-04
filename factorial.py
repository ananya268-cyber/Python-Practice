num = int(input("Enter the number of which you want the factorial"))
fact = 1
for i in range(1,number+1):
		fact *= i
		i += 1
print(f"The factorial of {number} is {factorial}")