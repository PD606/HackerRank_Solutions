def partition(low,high,arr):
    p=arr[low]
    # print(p)
    i=int(low)
    j=int(high)-1

    while(i<j):
        while((i<(len(arr)-1)) and (arr[i]<=p)):
            print('pkp')
            i+=1

        while(arr[j]>=p and j>low):
            # print(j)
            j-=1

        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]
        # print(arr)

    arr[low],arr[j]=arr[j],arr[low]
    # print(arr)

    print(j)
    return j

def quickSort(low,high,arr):

    if(low<high):

        mid=partition(low,high,arr)
        quickSort(low,mid,arr)
        quickSort(mid+1,high,arr)

    return arr

a=quickSort(0,6,[3,7,8,9,10,5])
# a=quickSort(0,6,[10,7 ,8,9,1,5])

# a=quickSort(0,9,[10,16,8,12,15,6,3,9,5])

print(a)





