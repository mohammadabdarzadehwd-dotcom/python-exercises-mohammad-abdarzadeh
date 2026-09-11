s=input('Enter String :')
l=s.lower().split()
l2=['hack','fraud','scam','password','atack']
c=0
for i in l2:
    c=l.count(i)
    if c>0:
     print(i, '->' , c)      
if c==0:
 print('No Word Found.')
