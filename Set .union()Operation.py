# Enter your code here. Read input from STDIN. Print output to STDOUT4
m=int(input())
l1=(input().split(' '))

n=int(input())
l2=(input().split(' '))

l1=set(l1)
l2=set(l2)

l3=l1.union(l2)

print(len(l3))


