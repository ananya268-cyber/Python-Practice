
n = int(input("Enter the number of rows: ")) 
for i in range(1, n+1):   # include n
    for j in range(1, i+1):   # print stars equal to row number
        print('*', end="") 
    print()
