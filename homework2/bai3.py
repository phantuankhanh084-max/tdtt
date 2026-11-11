a,b,c=map(int,input("nhap 3 canh cua tam giac: ").split())
if a<=b+c and b<=a+c and c<=b+a:
    if a==b==c:
        print('day la tam giac deu')
    elif a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==b**2+a**2:
            print("day la tam giac vuong")       
    elif a==b or b==c or c==a:
        print('day la tam giac can')
    else:
         print('day la tam giac thuong')
else:
     print('day khong phai 3 canh cua tam giac')
    

    