from helpers import alphabet_position, rotate_character
            

#This will take a string (sentence) and an integer.
#Turn the incoming string into a list
#Create a for loop that will cycle through each character in the string.
#With each character, pass it through the rotate_character function above, along with the integer
# value for rotation
#Create a new list and append each new character to the new list
def encrypt(text, rot):
    old_list = list(text)
    new_list= []
    for items in old_list:
        char = rotate_character(items, rot)
        new_list.append(char)
    encrypt = "".join(new_list)    
    return encrypt

def main():
    user_pass = input("What is your password?")
    user_rot = int(input("How many encryption cycles would you like?"))
    print(encrypt(user_pass, user_rot))   

if __name__ == "__main__":
    main()    