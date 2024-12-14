import string
import random
length = int(input("Enter password length: "))
password = []
characterList = string.ascii_letters + string.digits + string.punctuation
for i in range(length):
    randomchar = random.choice(characterList)
    password.append(randomchar)
 
print("The random password is " + "".join(password))