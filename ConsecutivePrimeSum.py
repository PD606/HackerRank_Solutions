# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input())
i=0

while(i<T):
    c=0
    l=[2]
    i+=1
    n=int(input())

    for f in range(2,n+1):
        for j in range(2,f):
            if(f%j==0):
                c=0
                break
            else:
                c=1
                continue        
        if(c==1):
            l.append(f)
        else:
            pass
    print(l)

    # print(len(l))
    k=len(l)-1
    m=[]

    while(k>0):
        s=0
        for d in range(0,k+1):
            if(s == l[k]):
                m.append(s)
                break

            elif(s>l[k]):
                break

            else:
                s=s+l[d]
        k-=1

    print(m)
    
        







