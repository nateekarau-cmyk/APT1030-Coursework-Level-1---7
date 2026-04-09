class Patient:

    def __init__(self, name, policy_number):
        self.name = name
        self.policy_number = policy_number

    def calculateClaim(self, amount):
        claim = amount - (amount * 0.10)
        return claim


name = input("Enter patient name: ")
policy = input("Enter policy number: ")
amount = float(input("Enter claim amount: "))

patient1 = Patient(name, policy)

final_claim = patient1.calculateClaim(amount)

print("Patient Name:", patient1.name)
print("Policy Number:", patient1.policy_number)
print("Final Claim Amount:", final_claim)