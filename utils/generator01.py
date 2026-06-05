from secrets import choice,SystemRandom
from typing import List
import string

class PasswordGenerator:
    def __init__(self,
                 length:int,
                 upper = True,
                 lower = True,
                 digit = True,
                 symbols = True
                 ):
        self.length = length
        self.feature = {"uppercase":upper,"lowercase":lower,"digit":digit,"digits":symbols}
    def build_charset(self): 
        "Creates a Collection of chars"
        self.char_set = {
            "uppercase":string.ascii_uppercase
            "lowercase":string.ascii_lowercase
        }
        self.collection = ""



