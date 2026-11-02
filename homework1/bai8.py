t=input("nhap ten chu ho: ")
a=int(input("nhap so chi dien ke thang truoc: "))
b=int(input("nhap so chi dien ke thang nay: "))
c=b-a
m=50*1984
n=50*2050
p=100*2380
q=100*2998
h=100*3350
if c<=50:
    print("ho va ten: ",t)
    print("tien phai tra la: ", int(c*1984*1.08))
elif 50<c<=100:
    print("ho va ten: ",t)
    print("tien phai tra la: ", int((m+(c-50)*2050)*1.08))
elif 100<c<=200:
    print("ho va ten: ",t)
    print("tien phai tra la: ", int((m+n+(c-100)*2380)*1.08))
elif 200<c<=300:
    print("ho va ten: ",t)
    print("tien phai tra la: ", int((m+n+p+(c-200)*2998)*1.08))
elif 300<c<=400:
    print("ho va ten: ",t)
    print("tien phai tra la: ", int((m+n+p+q+(c-300)*3350)*1.08))
elif 400<c:
    print("ho va ten: ",t)
    print("tien phai tra la: ", int((m+n+p+q+h+(c-400)*3460)*1.08))