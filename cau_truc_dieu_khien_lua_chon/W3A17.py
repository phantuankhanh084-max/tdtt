a,b,c,d=map(int,input().split())
if b/a==c/b==d/c:
    print('yes')
elif b==c==d==0:
    print('yes')
else:
    print('no')