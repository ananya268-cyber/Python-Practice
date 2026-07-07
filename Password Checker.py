attempt = 1

while attempt <= 3:
    password = input("Enter Password: ")

    if password == "Python123":
        print("Access Granted!")
        break

    print("Incorrect Password. Try Again.")
    attempt += 1
else:
    print("Account Locked!")