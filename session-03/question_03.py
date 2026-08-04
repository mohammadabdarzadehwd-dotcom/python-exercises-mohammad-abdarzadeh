SumOfNembers=0
SumTotal=0

for i in range (1,11):
    if i%2==0:
        SumOfNembers=i+5
        print(i ,'+' , 5 , '=' ,SumOfNembers)
        SumTotal+=SumOfNembers
        i+=1
    else:
        SumOfNembers=i*5
        print(i ,'*' , 5 , '=' ,SumOfNembers)
        SumTotal+=SumOfNembers
print('Sum Of Numbers Is :' , SumTotal)
        
        