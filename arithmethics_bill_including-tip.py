#WAP to split the total bill, including the tip
# input: bill, number of people, tip percentage

bill = int(input("Enter the Total amount on bill: "))
n = int(input("Enter the number of people to split among: "))
t = float(input("Enter percentage of tip: "))

bill+= ((bill*(t/100)))

print("Split on bill, including tip : ",bill/n)
