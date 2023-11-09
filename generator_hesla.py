# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# special_char = ['%', '#', '$', '!', '&', '(', ')', '*', '+', '?']

import random
import string

letters = string.ascii_letters
numbers = string.digits
special_char = '%#$!&()*+?'

print("Toto je generátor náhodného hesla. Heslo musí mít alespoň 8 znaků a obsahovat alespoň 2 kategorie znaků(písmeno, číslo, speciální znak)")
num_of_letters = int(input("kolik písmen chcete mít ve svém hesle?\n"))
num_of_numbers = int(input("kolik čísel chcete mít ve svém helse?\n"))
num_of_special_char = int(input("kolik speciálních znaků chcete mít ve svém hesle?\n"))

total_length = num_of_letters + num_of_numbers + num_of_special_char

#podmínka že obsahuje 1 znak z každé kategorie a dohromady nejméně 8 znaků
if num_of_letters < 1 or num_of_numbers < 1 or num_of_special_char < 1 or total_length < 8:
    print("Heslo musí obsahovat alespoň jeden znak z každé kategorie: písmena, číslice a speciální znaky. A musí obsahovat alespoň 8 znaků")
else:
    #generátor random hesla
    password = []

    for i in range(num_of_letters):
        password.append(random.choice(letters))

    for i in range(num_of_numbers):
        password.append(random.choice(numbers))

    for i in range(num_of_special_char):
        password.append(random.choice(special_char))

    # náhodně promíchat charaktery
    random.shuffle(password) #tady je to pořád list

    # převod hesla do stringu
    password = "".join(password)
    print(f"Vaše vygenerované heslo je: {password}")