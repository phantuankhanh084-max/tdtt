a=int(input())
s=[]
for i in range(1,a+1):
    s.append('*'*i+'*'*(i-1))
print('\n'.join(s))