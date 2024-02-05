# Random Password Generator

import random 
import string

def generate_password(length8):
    # Defining the characters to be used in the password
    characters = string.digits + string.ascii_letters + string.punctuation

    # generate any password of specified length
    pswd = ''.join(random.choice(characters) for _ in range(length))
    return pswd

if __name__ == "__main__" :
    pswd_length = int(input("Type and enter the required length of the password : "))

    if pswd_length <= 0 :
        print("Input Error. Enter a positive number")
    else :
        print("Your Password is : ", generate_password(pswd_length))

