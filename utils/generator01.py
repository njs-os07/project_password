from secrets import choice,SystemRandom
from typing import List
import string
from math import log2

class PasswordGenerator:
    CHAR_SET = {
            "uppercase":string.ascii_uppercase,
            "lowercase":string.ascii_lowercase,
            "digit":string.digits,
            "punctuation":string.punctuation
        }
    def __init__(self,length:int,upper = True,lower = True,digit = True,symbols = True):

        self.length = length
        self.feature = {"uppercase":upper,"lowercase":lower,"digit":digit,"punctuation":symbols}

    def build_charset(self): 
        "Creates a Collection of chars"
        self.collection = "" 
        for k,v in self.feature.items():
            if v:
                self.collection += self.CHAR_SET[k] 
        #print(self.collection) 

    def create_password(self) -> str:
        self.password = [choice(self.collection) for _ in range(self.length)] 
        SystemRandom().shuffle(self.password)
        return "".join(self.password)

    def calculate_entropy(self,password:str)->int:
        "Checks the Password strength"
        upper_cnt = lower_cnt = digit_cnt = punctuation_cnt = 0
        strlen = len(password)
        for i in password:
            if i.isalpha():
                if i.isupper: upper_cnt+=1
                else : lower_cnt +=1
            elif i.isdigit(): digit_cnt +=1
            else: punctuation_cnt+=1  
        entropy = strlen*log2(len(self.collection))
        return entropy

    def interpret_strength(self,entropy)->str:
        self.entropy = entropy
        "Estimating the Strength of the password using entropy"
        if self.entropy < 40: return "Weak"
        elif (self.entropy >= 40 and self.entropy < 60) : return "Moderate"
        elif (self.entropy >= 60 and self.entropy < 80) : return "Strong"
        else: return "Strong"

if __name__ == "__main__":
    obj = PasswordGenerator(16)
    obj.build_charset()
    password = (obj.create_password())
    print(password)
    #password = ":?^r}97Y"
    enp = obj.calculate_entropy(password)
    #print(password,enp,sep = '\n')
    print(obj.interpret_strength(enp))
    