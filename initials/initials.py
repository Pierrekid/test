def get_initials(fullname):
    Mspace = fullname.find(" ")
    Lspace = fullname.rfind(" ")
    midIni = Mspace + 1
    lastIni = Lspace + 1
    Ini = fullname[0] + fullname[midIni] + fullname[lastIni]
    initials = Ini.upper()
    if " " not in fullname:
        Ini= fullname[0] 
        initials = Ini.upper()
    elif Mspace == Lspace:
        Ini= fullname[0] + fullname[midIni]
        initials = Ini.upper()
    return initials
def main():
    user_input= input( "What is your full name?")
    print("The initials of", user_input, "are", get_initials(user_input))
if __name__ == '__main__':
    main()


