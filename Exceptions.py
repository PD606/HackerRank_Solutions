# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
i=0
while(i<n):
    i+=1
    try:
        m,k=map(int,input().split(' '))
        print(m//k)
    except Exception as e:
        print('Error Code:',end='')
        print('',e)
