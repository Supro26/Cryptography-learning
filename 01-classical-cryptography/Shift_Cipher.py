import random
def Encription(p,k):
    C=""
    for i in p:
        if(i.isupper()):
            C+=chr(((ord(i)-ord('A')+k)%26)+ord('A'))
        else:
            C+=chr(((ord(i)-ord('a')+k)%26)+ord('a'))
    C+=chr(k+65);
    return C
p=input("Enter the String: ")
k=random.randint(1,25)
encripted=Encription(p,k)
print(encripted);
