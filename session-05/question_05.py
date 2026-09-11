s=input('Enter String :')
l=s.split()
l2=l[0]
c=0
for i in l:
    if len(i)>len(l2):
     l2=i     
c=len(l2)
     
print(l2)
print('Length :' , c)         
    
