import random
import string

_strong = string.ascii_letters + string.digits + '!#@$&*%'
_alphanumeric = string.ascii_letters + string.digits
_alphabetic = string.ascii_letters
_numeric = string.digits

'''
Give random numeric string for given length
'''
def get_random_numeric_string(length=8):
    return "".join(random.choice(_numeric) for _ in range(length))
'''
Give random alphabetic string for given length
'''
def get_random_alphabetic_string(length=8):
    return "".join(random.choice(_alphabetic) for _ in range(length))

'''
Give random alphanumeric string for given length
'''
def get_random_alphanumeric_string(length=8):
    return "".join(random.choice(_alphanumeric) for _ in range(length))

'''
Give random all ascii character string for given length
'''
def get_random_strong_string(length=8):
    return "".join(random.choice(_strong) for _ in range(length))