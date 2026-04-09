# Python Parser Implementation of a Mini DSL for Mobile Money Rules

""" The program reads the transaction 
command entered by the user.
The command is split into parts using spaces.
The program then extracts the amount, sender, 
and receiver from the command.
After that, it checks if the balance 
is greater than the required amount.
If the balance is enough, the transaction is successful. 
Otherwise, the transaction fails. """

command = input("Enter transaction command: ")

balance = 6000

parts = command.split()

amount = int(parts[1])
sender = parts[3]
receiver = parts[5]
condition = int(parts[9])

print("Amount:", amount)
print("Sender:", sender)
print("Receiver:", receiver)

if balance > condition:
    print("Transaction Successful")
else:
    print("Insufficient Balance")