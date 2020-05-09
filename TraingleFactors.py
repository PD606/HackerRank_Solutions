def factors(n):
    i=1
    c=0
    while(i*i <= n):
        if(n%i==0):
            c+=2
        i+=1
    return c

t=True
num=1
nextnum=2

while(t):
    if(factors(num)>500):
        print(num)
        t=False

    else:
        num+=nextnum
        nextnum+=1




