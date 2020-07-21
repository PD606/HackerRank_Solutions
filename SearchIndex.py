m,n = map(int,(input()).split(' '))
arr=[]

for i in range(0,m):
    l=[]
    for j in range(0,n):
        ele=input()
        l.append(ele)
    arr.append(l)

# print(arr)

key=int(input())

for i in range(0,m):
    for j in range(0,n):
        if(int(arr[i][j]) == int(key)):
            # print(i+1)
            # print(j+1)
            print('({},{})'.format(i,j))