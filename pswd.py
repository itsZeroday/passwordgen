import secrets
import string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

print('Enter the password length')
password_length = int(input())
while True:
    password = ''
    for i in range(password_length):
        password += ''.join(secrets.choice(alphabet))

    if (any(char in special_chars for char in password) and 
        sum(char in digits for char in password)>4): 
            break

print(password)
