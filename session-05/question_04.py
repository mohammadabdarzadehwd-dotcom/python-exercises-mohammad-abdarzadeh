s=input('Enter String :')
l=s.split()
l2=[]
c=0
n=0
for i in l:
    c=s.count(i)
    l2=i
    if c>1:
     n=c
     l2=i 
print(l2 ,'->' , c)         
    
