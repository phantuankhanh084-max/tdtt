def dien_tich_trong_hoa(a,b):
    c=((a/2)**2)*3.14
    d=a*b
    e=d-c
    round(e,2)
    return "dien tich phan trong hoa la",e
n,m=map(int,input().split())
s=dien_tich_trong_hoa(m,n)
print(s)