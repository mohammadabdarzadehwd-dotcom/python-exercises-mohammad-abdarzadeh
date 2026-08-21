import random
m=random.randint(0,100)
while True:
    userint=int(input(' enter number :'))
    if userint<m:
        print('عدد را بزرگتر کن')
    elif userint>m:
        print('عدد را کوچکتر کن')
    else:
        print(' درست حدس زدی')  
        print('عدد تولیدی توسط کامپیوتر :' , m)
        break
    