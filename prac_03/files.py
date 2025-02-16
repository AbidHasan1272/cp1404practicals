"""CP1404/CP5632 Practical
Program:Appropriate choice of file-reading technique
Student Name:Abid Hasan
Date:16/02/2025

 """
# 1.

out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)
out_file.close()

# 2.

out_file = open("name.txt", "r")
name = out_file.read().strip()
out_file.close()
print(f"Hi {name}!")

# 3.
with open("numbers.txt" ,"r") as file:
    num_1 = int(file.readline().strip())
    num_2 = int(file.readline().strip())
sum=num_1+ num_2
print(sum)

# 4.
with open("numbers.txt","r") as file:
    for line in file:
        sum+=int(line.strip())
print(sum)



