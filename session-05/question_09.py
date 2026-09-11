l=['mohammad','13671367']
c=3
for i in range(0,3):
    username=input('Enter Username :')
    password=input('Enter Password :')
    if l[0]!=username and l[1]!=password:
        c-=1
        print('Wrong username or password')
        print('Atempts remaining: ' , c)
    else:
        print('Login successful')
        break
