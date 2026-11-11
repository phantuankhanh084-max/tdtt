x,y=map(float,input('nhap toa do: ').split(','))
r=int(input('nhap ban kinh: '))
a,b=map(int,input('nhap toa do diem:').split(','))
k=(a-x)**2+(b-y)**2
if k == r**2:
    print('diem do thuoc duong tron')
else:
    print('diem do khong thuoc duong tron')
