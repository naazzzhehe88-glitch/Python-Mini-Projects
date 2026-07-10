import random
import string

charValue = string.ascii_letters + string.digits + string.punctuation

password_len = int(input("Enter the length of the password"))

password = ""

for i in range(password_len):
    password+= random.choice(charValue)

print("Generated password is : ", password)