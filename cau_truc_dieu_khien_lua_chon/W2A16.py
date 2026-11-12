a=float(input())
if a>0:
    print(a-a%1+1,a-a%1,end=" ")
    if a%1>=0.5:
        print(a-a%1+1)
    else:
        print(a-a%1)
elif a<0:
    print(a-a%1+1,a-a%1,end=" ")
    if a%1<=0.5:
        print(a-a%1)
    else:
        print(a-a%1+1)
else:
    print('0 0 0')