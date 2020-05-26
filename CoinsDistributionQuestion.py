N=int(input())
o=0
t=0
f=0

if(N>4):
    n1=N-4
    f=n1//5
    rem=n1%5
    s=rem+4

if(s%2==0):
    o+=2
    s-=2
else:
    s-=1
    o+=1

t=s//2

print('Five = {}'.format(f))
print('Two =  {}'.format(t))
print('One  = {}'.format(o))









