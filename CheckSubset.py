T=int(input())
i=0
while(i<T):
    m=int(input())
    s1=input().split(' ')
    n=int(input())
    s2=input().split(' ')
    i+=1
    s1=set(s1)
    s2=set(s2)
    print(s1.issubset(s2))
