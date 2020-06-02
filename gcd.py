#code
T=int(input())
p=0

while(p<T):
    p+=1
    n1=int(input())
    n2=int(input())
    a=[1,n1]
    b=[1,n2]

    c=1
    
    j=2
    k=2

    while(j<=n1//0.5 ):
        if(n1%j==0):
            a.append(j)
        j+=1

    while(k<=n2//0.5):
        if(n2%k==0):
            b.append(k)
        k+=1

    a=set(a)
    b=set(b)
    print(a)
    print(b)

    ele=a.intersection(b)
    print(max(ele))




    
