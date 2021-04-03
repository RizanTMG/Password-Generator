# Password generator

'''
This is not actually password generator!
It just selects words and number randomly from a list to make it less likely to be gussed in a brit force attack!

length manditory
numeric optional
strength optional
lenght, num = False (deafult), strngth = (weak, strong, very)
'''

import random, string

def password(length, num = False, strength = "weak"):
        '''length of password, if you want a number, and strength(weak, strong, very)'''
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        letters = lower + upper
        dig = string.digits
        punc = string.punctuation
        pwd = ''
        if strength == "weak":
            if num:
                length -= 2
                for I in range(2):
                    pwd += random.choice(dig)
            for I in range(length):
                pwd += random.choice(lower)
        elif strength == "strong":
            if num:
                length -= 2
                for I in range(2):
                    pwd += random.choice(dig)
            for I in range(length):
                pwd += random.choice(letters)
        elif strength == "very":
            ran = random.randint(2, 4)
            if num:
                length -= 2
                for I in range(ran):
                    pwd += random.choice(dig)
            length -= ran
            for I in range(ran):
                pwd += random.choice(punc)
            for I in range(length):
                pwd += random.choice(lower)
        
        pwd = list(pwd)
        random.shuffle(pwd)
        print(''.join(pwd))
             
# Asks the length of the password
print("Enter the length of the password:")
number = input("> ")

# Converts input into number(integer)
try:
    number = int(number)
except:
    print("Please enter a number")
    
# Asks if to input number or not
print("\n Should the password contain number:")
numeric = input("(Y/N)> ")
numeric = numeric.upper()
if numeric == "Y":
    numeric = True
elif numeric == "N":
    numeric = False
    
# Choose the mode
print("\n Choose a mode:")
print("1. Weak")
print("2. Strong")
print("3. Very strong \n")
command = input("> ")
if command == "1":
    strength = "weak"
elif command == "2":
    strength = "strong"
elif command == "3":
    strength = "very"
else:
    print("Invalid options!")
password(number, numeric, strength)
