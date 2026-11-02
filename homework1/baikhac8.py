a=int(input("nhap so nam:"))
if a <= 0:
    print("a khong hop le")
else:
    if (a % 400 == 0) or (a % 4 == 0 and a % 100 != 0):
        print(a," la nam nhuan")
    else:
        print(a," khong phai la nam nhuan")    