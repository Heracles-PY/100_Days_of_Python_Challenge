import string
import random

letters = list(string.ascii_letters)   # a-z and A-Z
numbers = list(string.digits)          # 0-9
symbols = list(string.punctuation)     # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

print("Welcome to the password generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like?\n"))
num_symbols = int(input("How many symbols would you like?\n"))

password_list = []
for i in range(num_letters):
    password_list.append(random.choice(letters))
for i in range(num_numbers):
    password_list.append(random.choice(numbers))
for i in range(num_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = "".join(password_list)

print(f"Your password is: {password}")