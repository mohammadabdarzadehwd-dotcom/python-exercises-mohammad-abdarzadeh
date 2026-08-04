AB=float(input('Enter Account Balance :'))
WA=float(input('Enter The Withdrawal Amount :'))
if WA<0:
    print('عملیات با خطا مواجه شد')  
elif AB>WA:
        AB=AB-WA
        print('عملیات برداشت انجام شد')
        print('موجودی حساب :' , AB)
else:
       print('موجودی کافی نمی باشد')
