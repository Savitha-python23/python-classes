import string, secrets
# print(dir(string))
s = input("Enter your name")
rev = s[::-1]
#  a = string.punctuation 
a = secrets.token_hex()
print(rev+a)