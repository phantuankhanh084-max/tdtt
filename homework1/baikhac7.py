a=int(input("nhap diem hoc sinh"))
if a < 0 or a > 10:
    print("a khong hop le! Vui long nhap diem trong khoang 0 den 10")
else:
    if a >= 8.0:
        print("hoc luc: tot")
    elif a >= 6.5:
        print("hoc luc: kha")
    elif a >= 5.0:
        print("hoc luc: trung binh")
    else:
        print("hoc luc: yeu")
