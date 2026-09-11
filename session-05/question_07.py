s=input(' Enter String :')
l=list(s)
l2=[]
c=1
for i in range (len(l)-1):
       if l[i]==l[i+1]:
           c+=1
       else:
           l2.append(l[i])
           l2.append(str(c))
           c=1
l2.append(l[i+1]) 
l2.append(str(c))        
print(''.join(l2))      
