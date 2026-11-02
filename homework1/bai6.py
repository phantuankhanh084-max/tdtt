from math import*
a,b,c=map(int,input("nhap 3 canh cua tam giac: ").split())
if a<=b+c and b<=a+c and c<=b+a:
    p=(a+b+c)/2
    s=sqrt(p*(p-a)*(p-b)*(p-c))
    round(s,1)
    print("dien tich cua hinh tam giac la:",s)
else:
    print("khong phai 3 canh cua tam giac")