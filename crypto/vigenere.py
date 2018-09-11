from helpers import alphabet_position, rotate_character
            

#This will take a string (sentence) and an integer.
#Turn the incoming string into a list
#Also turn the key into a list that can pass through index function
#Pass the letters from the text list and the index together in the rotate_character function
#Append the new letter to a a brand new list.
#If the key is not long enough, reset the key position to 0.
#Join new list together wih join method
#Return.
import string

def encrypt(text,key):
    r = string.ascii_lowercase
    x = string.ascii_uppercase
    combo = r + x
    old_list = list(text)
    key = list(key)    
    Nkey_list= []
    final_list = []
    for kletters in key:
        f = alphabet_position(kletters)
        Nkey_list.append(f)
     
    x = 0
    for items in old_list:
        if items in combo:
            t = rotate_character(items, Nkey_list[x])
            final_list.append(t)
            x += 1
            if x >= len(Nkey_list):
                x= 0    
        else:
            final_list.append(items)
    encrypt = "".join(final_list)    
    return encrypt

def main():
    user_pass = input("What is your password?")
    user_key = (input("What would you like your encryption key to be?"))
    print(encrypt(user_pass, user_key))   

if __name__ == "__main__":
    main()
        
        
   
