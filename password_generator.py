import random
import string
letters = list(string.ascii_letters)
digits = list(string.digits) 
symbols = list(string.punctuation) 
all_chars=letters + digits + symbols
your_password=""
try:
    length=int(input("Determine password length:"))
    if length <= 0:
        print("Length must be positive!")
    raise SystemExit
except ValueError:
    print("Please enter a number!")
for i in range(length):
    chars=random.choice(all_chars)
    your_password=your_password+chars
print(f"Your password:{your_password}")