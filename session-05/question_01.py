password=input('Enter yoyr password : ')
Uppercase=0
Lowercase=0
Digit=0
Symbol=0

if len(password) < 8:
  print('Password must contain at least 8 characters') 
for i in password :
 if i.isupper():
     Uppercase=1   
 if i.islower():
     Lowercase=1     
 if i.isdigit():
     Digit=1     
 if i=='@' or i=='#' or i=='$' or i=='%':
     Symbol=1
      
if Uppercase < 1:
  print('Password must contain a Capital Letters')     
elif Lowercase < 1:
  print('Password must contain a Lowercase Letters')     
elif Digit < 1:
  print('Password must contain a Digit')    
elif Symbol < 1:
  print('Password must contain a Special Symbol')   
else:
    print('Password Is Valid')
    
    

     
     
