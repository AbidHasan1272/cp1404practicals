MIN= 10
enter_pass = input("Enter password:")
while len(enter_pass)< MIN:
    print("*" * len(enter_pass))
    print("Invalid Password")
    enter_pass =input("Enter password:")



