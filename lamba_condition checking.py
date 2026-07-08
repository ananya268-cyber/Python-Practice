age = int(input("Enter your age: "))
check = lambda age: "Invalid input" if age < 0 else "Adult" if age > 18 else "Teenager" if age <= 18 and age >= 13 else "Child"
print(check(age))