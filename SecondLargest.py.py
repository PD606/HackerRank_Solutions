T=int(input())
i=0
while(i<T):
    n=int(input())
    l=list(map(int,input().split(' ')))
    # l=input().split(' ')
    # l=map(int,list(l))
    l.sort()
    j=-2
    ele=l[-1]
    # print(ele)
    if(ele == l[-2]):
        while(l[j] == ele):
            j-=1
        print(l[j])
    else:
        print(l[-2])
        
    # print(l)
    i+=1
    
    