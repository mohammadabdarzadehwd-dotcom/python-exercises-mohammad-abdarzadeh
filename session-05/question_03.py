s=input('Enter String :')
L=len(s)
Leters=0
Uppercase=0
Lowercase=0
Digits=0
Spaces=0
SpecialChar=0
for i in s:
    #if i.isalpha():
      #  Leters+=1
    if i.isupper():
           Uppercase+=1
    if i.islower():
           Lowercase+=1
    if i.isdigit():
        Digits+=1
    if i==' ':
        Spaces+=1    
    else:
        SpecialChar=L-(Uppercase+Lowercase+Digits+Spaces)
print('Leters =' , Uppercase+Lowercase)        
print('Uppercase =' , Uppercase)        
print('Lowercase =' , Lowercase)        
print('Digits =' , Digits)        
print('Spaces =' , Spaces)        
print('SpecialChar =' , SpecialChar)        
        