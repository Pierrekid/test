#Create function that changes all letters to one case.
# after chnaging case, print the index position of that letter with regard to the ascii method.
# look up how to pull index of string
import string

def alphabet_position(letter):
    r = string.ascii_lowercase
    x = string.ascii_uppercase
    if letter in x:
        y = x.index(letter)
        return y
    else:
        if letter in r:
            y = r.index(letter)
            return y
            


#repear what i did above 
#After finding index, add the second argument (rot) to it.
#If total is above 25, is the % function to get new number.
# Use the number to look up position of letter in the ascii string
#return the letter
#Put statement in to ignore none characters

def rotate_character(char, rot):
    x = string.ascii_uppercase
    y = string.ascii_lowercase
    combo = x + y
    if char not in combo:
        return char
    else:
        p = alphabet_position(char)
        new_let = p + rot
        if new_let >= 26:
            new_let= new_let % 26
            if char in x:
                letter = x[new_let]
                return letter
            else:
                if char in y:
                    letter = y[new_let]
                    return letter
        else:
            if char in x:
                letter = x[new_let]
                return letter
            else:
                if char in y:
                    letter = y[new_let]
                    return letter