import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
email = input("Masukkan Email: ")

def validate(email):
    if(re.match(regex,email)):
        return 'Valid'
    else:
        return 'INVALID!'

print(validate(email))