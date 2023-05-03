#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
'h'
, 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
random.shuffle(letters) 
random.shuffle(symbols)
random.shuffle(numbers)

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
print("")
print("")

total_password = []
for i in range(0,nr_letters):
  total_password.append(random.choice(letters))

for j in range(0,nr_symbols):
  total_password.append(random.choice(symbols))

for k in range(0,nr_numbers):
  total_password.append(random.choice(numbers))
random.shuffle(total_password)

print(total_password)
overall_password = ""
for char in total_password:
  overall_password += char
print(overall_password)
