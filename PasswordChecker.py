import re

def password_checker(password):
    length_error = "Password must be at least 8 characters long."
    complexity_error = "Password must contain at least 1 lowercase letter, 1 uppercase letter, 1 digit and 1 special character."
    common_error = "Password was found in a common list. Try making the password more unqiue"
    match = re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password)

    with open('common.txt', 'r') as f:
        common = f.read().splitlines()
        
    

    if len(password) < 8:
        return length_error
    elif password in common:
        return common_error
    elif match is None:
        return complexity_error
    else:
        return "Password is valid."

password = input("Enter a password: ")
print(password_checker(password))