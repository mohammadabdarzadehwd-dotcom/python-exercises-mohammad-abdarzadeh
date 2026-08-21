import random
while True:
        m=random.choice(['sang' , 'kaghaz' , 'gheichi'])
        print(m)
        userstr=input(' enter sang or kaghaz or gheichi :')
        if userstr=='sang' and m=='gheichi':
            print('کاربر برنده است')
        elif userstr=='sang' and m=='kaghaz':
            print('کامپیوتر برنده است')
        elif userstr=='kaghaz' and m=='sang':
            print('کاربر برنده است')
        elif userstr=='kaghaz' and m=='gheichi':
            print('کامپیوتر برنده است')    
        elif userstr=='gheichi' and m=='kaghaz':
            print('کاربر برنده است')
        elif userstr=='gheichi' and m=='sang':
            print('کامپیوتر برنده است')       
        elif userstr==m:
            print('تساوی')
            continue
        elif userstr=='exit':
             break
        else:
             print('لطفا از لیست انتخاب کن')
      
    