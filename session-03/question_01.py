l=[15,50,70,1,90,20,4,108,6]
maxNumber=0
for i in range (0,8):
    if maxNumber>l[i]:
        i+=1
    else:
        maxNumber=l[i]
print('MAX Number Is :' ,maxNumber)        
 '''       
for number in l:
     if number>maxNumber:   
         maxNumber=number
print(maxnumbe)         
         '''