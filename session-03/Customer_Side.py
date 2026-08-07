products=['book','pen']
print('Salam Be Foroshgahe FANAVARI_CO Khosh Amadid')
answer=input('aya mikhahid kharid konid? :')
answer=answer.lower()
answer=answer.strip(' ')

'''if answer=='yes':
    print('befarmaeed')'''

'''if answer=='yes':
    print('yaddasht mikonam')
else:
    print('besiar awli')    '''
    
    
    
if answer=='yes':
    print('yaddasht mikonam')
    products.append(input('name yek mahsol ra vared konid :'))
    print('products list is :' , products)
elif answer=='no':
    print('mamnoon')   
else:
    print('faghat ba yes/no javab bedahid')    
    
    
    
        