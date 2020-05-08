#code


T=int(input())
i=0
while(i<T):
    c=1
    i+=1
    a,b=map(int,input().split(' '))
    l=[1]
    for k in range(2,(a//2)+1):
        if(a%k==0):
            l.append(k)
        
    l.append(a)
    print(l)
    if(b<len(l)):
        print(l[-b])
    else:
        print(-1)
                
            
                    
                
        
        
    
    
    