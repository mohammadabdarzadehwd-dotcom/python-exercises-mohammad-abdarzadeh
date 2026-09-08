s=input('Enter String :')
l=''
for i in s:
    if i not in l:
        l+=i
print(l)
