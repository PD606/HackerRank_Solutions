# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
i=0
l1=[]
k=0
while(i<n):
    m=(input().split(' '))
    i+=1
    ch=int(m[0])
    try:
        if(m[1]!=None):
            ele=int(m[1])
    except:
        pass
  

    if(ch==1):
        if(ele>=k):
            l1.append(ele)
            k=ele
       

    elif(ch==2):
        if((len(l1))!=0):
            l1.pop()
          

    else:
        if(len(l1)!=0):
            p=max(l1)
            print(p)
           

