n = int(input("Enter a number: "))
func = [lambda arg=x: arg * 10 for x in range(1, n)]
for i in func:
    print(i())