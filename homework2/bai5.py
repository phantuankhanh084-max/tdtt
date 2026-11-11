from math import*
a,b,c=map(int,input('nhap lan luot he so: ').split())
d=b**2-4*a*c
if d<0:
    print('phuong trih khong co nghiem')
elif d==0:
    print('phuong trinh cos mot nghiem kep:',-b/(2*a))
else:
    e=sqrt(d)
    print('nghiem thu nhat la:',(-b-e)/(2*a))
    print('nghiem thu hai la:',(-b+e)/(2*a))
    