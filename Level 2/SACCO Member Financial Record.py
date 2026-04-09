name = input("Enter member name: ")
member_id = input("Enter member ID: ")

total_savings = 0

for i in range(1, 7):
    contribution = float(input("Enter contribution for month " + str(i) + ": "))
    total_savings = total_savings + contribution

print("Member Name:", name)
print("Member ID:", member_id)
print("Total Savings:", total_savings)