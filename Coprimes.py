# def isPrime(a,b):
#     p=1
#     for i in range(2,(a//2)):
#         if((a%i)==0):
#             p=0
#             break

#     for i in range(2,(b//2)):
#         if((b%i)==0):
#             p=0
#             break
    
#     return p

def gcd(a,b):

    i=j=1
    m=[a]
    n=[b]

    val=1

    if(((a%2)==0) and ((b%2)==0)):
        # print('oooo')
        return 0

    while(i<=(a//2)):
        if((a%i)==0):
            m.append(i)
            # i+=1
        i+=1

    while(j<=(b//2)):
        if((b%j)==0):
            n.append(j)
            # j+=1
        j+=1

    q=0
    
    # print(m)
    # print(n)
    m=set(m)
    n=set(n)
    s=m.intersection(n)
    return s

n= int(input('no'))

arr=[]
cp=0

for i in range(0,n):
    a=int(input())
    arr.append(a)

for i in range(0,n):
    for j in range(i+1,n):
        # prime=isPrime(arr[i],arr[j])
        # if(prime==1):
        #     cp+=1
        #     break
        res=gcd(arr[i],arr[j])
        # print(res)
        if(res=={1}):
            cp+=1

print(cp)
       
        
