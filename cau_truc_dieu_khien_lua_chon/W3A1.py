n=input()
if len(n)==3 and int(n)>0:
    n=int(n)
    a=n%10
    b=n%100//10
    c=n//100
    d=a*100+b*10+c
    print(d)
else:
    print('error')