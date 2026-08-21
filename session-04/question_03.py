while True:
    password=input('enter password :')
    if len(password) == 8 and password[:4].isalpha()  and password[4:].isdigit():
        print ('معتبر')
        print('Password Is :' , password)
        break
    else:
        print('نا معتبر :')
