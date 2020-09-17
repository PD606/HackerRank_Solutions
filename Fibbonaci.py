n=int(input('Enter how many numbers'))
c=2
first=0
second=1
print('0\n1')
while(c<n):
    third=first+second
    first=second
    second=third
    c+=1
    print(third)




