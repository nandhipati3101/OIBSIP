import random
import string
print("password generator:")
n=int(input("enter the length of the string:"))
print("customize your password by selecting yes(\"y\") or no(\"n\"):")
letters=input("need letters:").lower()=="y"
digits=input("need digits:").lower()=="y"
symbols=input("need symbols:").lower()=="y"
def generator(n,letters,digits,symbols):
    combo=""
    if letters==True:
        combo+=string.ascii_letters
    if digits==True:
        combo+=string.digits
    if symbols==True:
        combo+=string.punctuation
    if not combo:
        print("sorry! it is an invalid entry")
        return None
    password="".join(random.choice(combo) for _ in range(n))
    print("your Password is: ",password)
gained_password=generator(n,letters,digits,symbols)

