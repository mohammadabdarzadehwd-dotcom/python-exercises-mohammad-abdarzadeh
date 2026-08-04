Color1=input('Enter First color :')
Color2=input('Enter Second color :')
Color3=input('Enter Third color :')
Color1=Color1.upper()
Color2=Color2.upper()
Color3=Color3.upper()

if Color1==Color2 and Color1==Color3 and Color2==Color3:
    print('3 Color Are The Same')
elif    Color1==Color2 or Color1==Color3 or Color2==Color3:
    print('2 Color Are The Same')
else:
    print('The Color Are Not The Same')