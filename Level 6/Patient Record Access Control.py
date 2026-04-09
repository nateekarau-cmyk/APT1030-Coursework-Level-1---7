def checkAccess(role):
    if role != "Doctor":
        raise Exception("Access Denied")
    else:
        print("Access Granted")


role = input("Enter role: ")

try:
    checkAccess(role)
except Exception as e:
    print(e)

""" This program checks if the user role is Doctor. 
If not, the program raises an exception. 
The try-except block catches the error and prints 
an access denied message. """