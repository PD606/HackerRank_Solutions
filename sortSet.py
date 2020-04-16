# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())

l1=(input().split(' '))

n=int(input())

l2=(input().split(' '))
l1=set(l1)
l2=set(l2)
#c=[]
a=l1.difference(l2)
b=l2.difference(l1)

c=a.union(b)
c=(sorted(c,key=float))

c=list(c)

c='\n'.join(c)

print(c)



