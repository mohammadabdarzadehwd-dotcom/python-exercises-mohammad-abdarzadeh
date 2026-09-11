s=input('Enter String :')
char_list=list(s)
L=len(s)
input_list=s.split()
Leters=0
Uppercase=0
Lowercase=0
Digits=0
Spaces=0
SpecialChar=0

#______________________________________________


for i in s:
    if i.isupper():
           Uppercase+=1
    if i.islower():
           Lowercase+=1
    if i.isdigit():
        Digits+=1
    if i==' ':
        Spaces+=1    
    else:
        SpecialChar=L-(Uppercase+Lowercase+Digits+Spaces)


#_____________________________________________

Longest_word=input_list[0]
c=0
for i in input_list:    
    if len(i)>len(Longest_word):
     Longest_word=i     

#_____________________________________________


Shortest_word=input_list[0]
c=0
for i in input_list:
    for i in input_list:    
        if len(i)<len(Shortest_word):
         Shortest_word=i     

#_____________________________________________            



most_char = char_list[0]
max_count = 0

for j in char_list:
    c = char_list.count(j)

    if c > max_count:
        max_count = c
        most_char = j


#_____________________________________________


most_word = input_list[0]
max_word_count = 0

for k in input_list:
    c = input_list.count(k)

    if c > max_word_count:
        max_word_count = c
        most_word = k

#_____________________________________________


print('Totla Characters =' , len(s))        
print('Totla Words =' ,len(input_list))        
print('Total Leters =' , Uppercase+Lowercase)  
print('Total Digits =' , Digits)        
print('Total Spaces =' , Spaces)        
print('Total Uppercase =' , Uppercase)        
print('Total Lowercase =' , Lowercase)        
print('SpecialChar =' , SpecialChar)        
print('Longest word =' , Longest_word)        
print('Shortest word =' , Shortest_word)        
print('Most repeated character =' ,most_char )        
print('Most repeated word =' ,most_word )        



