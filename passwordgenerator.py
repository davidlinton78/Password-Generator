import random

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]
symbols = ["!","@","#","£","$","%","^","&","*","(",")","{","}","[","]","]","~","§","<",">"]
#Intro
print("Welcome To My Password Generator!")
#User input
user_letter = int(input("Please enter how many letters you would like!\n"))
user_numbers = int(input("Please enter how many numbers you would like!\n"))
user_symbols = int(input("Please enter how many symbols you would like!\n"))

password = []
#For loop 
for let in range(1, user_letter +1):
    letter = random.choice(letters)
    password += letter
for num in range(1, user_numbers +1):
    number = random.choice(numbers)    
    password += number
for sym in range(1, user_symbols +1):
    symbol = random.choice(symbols)    
    password += symbol
#shuffle password 
random.shuffle(password)
#join password together
generate = "".join(password)

print(f"Your new password is: {generate}, Please try and change your password regular! ")
