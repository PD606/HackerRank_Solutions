n=input().split(',')


d={
'Jan':'1',
'Feb':'2',
'Mar':'3',
'Apr':'4',
'May':'5',
'Jun':'6',
'Jul':'7',
'Aug':'8',
'Sep':'9',
'Oct':'10',
'Nov':'11',
'Dec':'12'

}

# print(d['Dec'])

for i in range(0,len(n)):

    for j in range(1,len(n)-i):
        y=n[j-1]

        y=y[7:]

        y1=n[j]
        y1=y1[7:]

        if((y) == (y1)):
            m=n[j-1]
            m=m[3:6]

            m1=n[j]
            m1=m1[3:6]

            # print(d[m])
            # print(d[m1])

            # for j in range(1,len(n)-i):.

            if((d[m]) == (d[m1])):

                dd=n[j-1]
                dd=dd[0:2]

                dd1=n[j]
                dd1=dd1[0:2]

                # print('daaay',dd)
                # print('dadadoa',dd1)

                # for j in range(1,len(n)-i):
                if(int(dd)<int(dd1)):
                    continue
                else:
                    n[j],n[j-1]=n[j-1],n[j]

            elif(d[m] < d[m1]):
                continue

            else:
                n[j-1],n[j]=n[j],n[j-1]

            
        elif(int(y)<int(y1)):
            continue

        else:
            n[j-1],n[j]=n[j],n[j-1]
        
print(n)
            
        
