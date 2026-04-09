def calculateClaim(amount):
    return amount - (amount * 0.10)


name = input("Enter patient name: ")
policy = input("Enter policy number: ")
amount = float(input("Enter claim amount: "))

final_claim = calculateClaim(amount)

print("Patient Name:", name)
print("Policy Number:", policy)
print("Final Claim Amount:", final_claim)