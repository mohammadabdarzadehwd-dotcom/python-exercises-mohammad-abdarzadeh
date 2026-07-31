t=int(input('Enter Time :'))
if t>=0 and t<=6:
    print('In The Morning')
elif t>=7 and t<=12:
    print('In The noon')
elif t>=13 and t<=18:
    print('In The Afternoon')
elif t>=18 and t<=23:    
    print('In The Night')
else:
    print('Invalid Time')
    
  
        