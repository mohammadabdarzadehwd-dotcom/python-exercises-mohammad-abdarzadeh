x=float(input('Enter First Number :'))
y=float(input('Enter Second Number :'))
o=input('Enter The Operator :')
Result=0
if o=='+':
    Result=x+y
    print('Result Is :' , Result)    
elif o=='-':
    Result=x-y
    print('Result Is :' , Result)    
elif o=='*':
    Result=x*y
    print('Result Is :' , Result)    
elif o=='/':
    Result=x/y
    print('Result Is :' , Result)    
else:
     print('The Operator Is Invalid')    

    
