import re
import math
strength=0
re=""
#the formual : length * log of 2 (char_set_size) that's it
char_set=[]
def checkpass(password):
    if len(password)>=8:
        strength+=1
    else:
        re+="Password must be at least 8 characters long.\n"
    if re.search("[a-z]",password):
        strength+=1
    else:
        re+="Password must contain at least one lowercase letter.\n"
    if re.search("[A-z]",password):
        strength+=1
    else:
        re+="Password must contain at least one uppercase letter.\n"
    if re.search("[0-9]",password):
        strenght+=1
    else:
        re+="Password must contain at least one digit.\n"
    if re.search("[!#@$%^&*()_+]",password):
        strength+=1
    else:
        re+="Password must contain at least one special character.\n"
    if strength==5:
         return "Password is strong."
    if strength>=3:
        return "Password is medium strength. " + re 
    else:
        return "Password is weak. " + re

def charset_size(password):
    size=0
    if re.search("[A-Z]",password):
        size+=26
    if re.search("[a-z]",password):
        size+=26
    if re.search("[0-9]",password):
        size+=10
    else:
        size+=33
    return size
def checkentopy(password):
    length = len(password)
    char_set_size=charset_size(password)
    entropy = length * math.log2(char_set_size)
    return entropy

#can u check it's efficiency ??
#efficiency means id
#i need frist know if it works or not 