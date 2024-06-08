import string
import random
plen = int(input("Enter the length of the password: "))
print('''Choose character set for password from these:
      1.Digits
      2.Letters
      3.Special characters
      4.Exit''')
characterlist = ""
while(True):
    choice = int(input("Enter your choice: \n"))
    match choice:
        case 1:
            characterlist += string.ascii_letters
        case 2:
            characterlist += string.digits
        case 3:
            characterlist += string.punctuation
        case 4:
            break
        case _:
            print("Please pick a valid option!")
if not characterlist:
    print("No character set selected!")
else:
    password = []
for i in range(plen):
    randomchar = random.choice(characterlist)
    password.append(randomchar)
print("Your random password is generated: " + "".join(password))
