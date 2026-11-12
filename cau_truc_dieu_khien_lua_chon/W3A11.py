a,b,c=map(int,input("nhap 3 canh cua tam giac: ").split())
if a<b+c and b<a+c and c<b+a and a>0 and b>0 and c>0:
    if a==b==c:
        print('tam giac deu')
    elif a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==b**2+a**2:
            print("tam giac vuong")       
    elif a==b or b==c or c==a:
        print('tam giac can')
    else:
         print('tam giac thuong')
else:
     print('khong phai tam giac')
    