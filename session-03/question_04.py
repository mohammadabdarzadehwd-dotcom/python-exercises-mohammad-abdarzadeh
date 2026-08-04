s=input('Enter String :')
c=0
c2=0
for i in s:
   c=c+1
print('Len Of String Is :' ,c)
if c%2==0:
    c=c//2
    for j in range(0,c):
        print(s[j], end='')
else:
    c2=c//2
    for j in range(c2,c):
        print(s[j], end='')

        