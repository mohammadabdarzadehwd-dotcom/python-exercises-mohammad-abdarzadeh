maxRecord=0
for i in range (0,10):
    height=float(input('Enter Height :'))
    if maxRecord>height:
        print('This Record Has Already Been Set :' , maxRecord)
        i+=1
    else:
        maxRecord=height
        print('A New Record Was Set')
        print('The Height Jump Recordde So Far :' , maxRecord)
#print('MAX Record Is :' ,maxRecord)        
        
        