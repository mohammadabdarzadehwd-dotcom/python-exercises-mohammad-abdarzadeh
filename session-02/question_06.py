p=int(input('Enter Price :'))
if p>1000000:
    p=p-(p*15/100)
elif p>=500000 and p<=1000000:
    p=p-(p*10/100)  
print('total Price Is :',p)    