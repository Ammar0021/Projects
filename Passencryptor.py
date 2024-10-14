def encrypt_password(password):
    encrypted_password = ""  
    
    # Letter Substitutions
    
    Lsub = {
        'a': 'q', 'b': 't', 'c': 's', 'd': 'w', 'e': 'v', 'f': 'r',
        'g': 'h', 'h': 'n', 'i': 'u', 'j': 'm', 'k': 'o', 'l': 'p',
        'm': 'j', 'n': 'g', 'o': 'l', 'p': 'k', 'q': 'a', 'r': 'y',
        's': 'x', 't': 'z', 'u': 'i', 'v': 'c', 'w': 'd', 'x': 'e',
        'y': 'f', 'z': 'h'
    }

    # Number Substitutions
    
    Nsub = {
        '1': '9', '2': '5', '3': '1', '4': '6', '5': '3', 
        '6': '8', '7': '4', '8': '0', '9': '7', '0': '2'
    }


    for character in password:

        if character in Lsub or character in Nsub:  # Check against both dictionaries

            if character in Lsub:

                encrypted_password += Lsub[character]  # Substitute using Lsub

            else:

                encrypted_password += Nsub[character]  # Substitute using Nsub
        
        else:
            encrypted_password += character

    return encrypted_password



userPassword = input("Please enter a password: ")

while True:
    
    confirm_password = input("Please confirm your password: ")
    
    if userPassword == confirm_password:
        
        break  # Exit the loop if passwords match
    
    else:
        
        print("Passwords do not match. Please try again.")

confirmPassword = input("Please confirm your password: ")

if userPassword != confirmPassword:
    
    print ("Passwords do no match, please try again")

else:

    Encryptedpass = encrypt_password(userPassword)


def strong_password_hints(): #Helps user create a strong password

    print ("Hints for creating a strong password:")
    print ("1. Use at least 6 characters")
    print ("2. Have uppercase and lowercase letters")
    print ("3. Have numbers in your password")



print(f"Your Encrypted Password is: {Encryptedpass}")



if len(userPassword) >= 6:
    
    print("Your password is strong!")
    


    ## Unfinished code here
else:
    
    print("Your password is weak.")

    strong_password_hints()
