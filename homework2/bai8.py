a,b,m,c,d,n=map(int,input('nhap lan luot caca gia tri:').split())
y=(c*m-a*n)/(b*c-a*d)
x=(m-b*y)/a
print('gia tri cua x la:',x)
print('gia tri cua y la:',y)