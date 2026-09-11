s=input('Enter String :')
l=s.split()
l2=l[0]
c=0
n=0
for i in l:
    c=l.count(i)
    l2=i
    if c>n:
     n=c
     l2=i 
print(l2 ,'->' , c)         
    
