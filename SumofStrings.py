#code
T=int(input())
p=0
while(p<T):
    p+=1
    n=input()
    tmp=''
    s=0

    for i in n:
        if(i.isdigit()):
            tmp+=i
        # print('yyyy',tmp)
        else:
        # print('pp',s)
            s+=int(tmp)
            tmp='0'

    print(s+int(tmp))

