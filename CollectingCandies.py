n=int(input('box'))
t=[]
l=list(map(int,input().split(' ')))

# print(l)

while(n>1):
    s=0
    l.sort()
    # print(l)

    ele1=l.pop(0)
    ele2=l.pop(0)

    # print(ele1)
    # print(ele2)

    s=int(ele1)+int(ele2)

    t.append(s)
    l.append(s)    
    n-=1

print(sum(t))



