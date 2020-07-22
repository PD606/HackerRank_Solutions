m,n = map(int,input().split(' '))

arr=[]


for i in range(0,m):
    l=[]
    for j in range(0,n):
        ele=int(input())
        l.append(ele)
    arr.append(l)

print(arr)

row=[]
col=[]
for i in range(0,m):
    row.append(arr[i][0])
    col.append(arr[i][1])


# print(row)
# print(col)
done=[]

for i in range(0,len(row)):
    for j in range(0,len(col)):
        if((row[i] == col[j]) and ((row[i]) not in done) and ((col[i]) not in done)):
            done.append(row[i])
            done.append(col[j])
            re=row[col.index(col[j])]
            ce =col[row.index(row[i])]
            # print(re)
            # print(ce)
            if(re == ce ):
                # print('loooo')
                print('({},{})'.format(row[i],re))
                # row.remove(re)
                # col.remove(ce)


        

