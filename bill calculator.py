print("-"*100)
print(f"\n{"\t"*4}Welcome to the Bill Calculator\n")
print("-"*100,"\n")

bill = float(input("Enter total amount of the bill : "))
people = int(input("Enter total no of people involved : "))

amt = bill/people*1.12

print(f"\n{"\t"*4}The amount to be paid by each person : $",amt)