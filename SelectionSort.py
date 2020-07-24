def selectionSort(arr):
    for i in range(0,len(arr)):
        min=arr[i]
        print(min)
        for j in range(i+1,len(arr)):
            if(min>arr[j]):
                min=arr[j]
                pos=arr.index(min)
        # print(arr[i])
        # print(arr[0])
        if(min==arr[j]):
            arr[pos],arr[i]=arr[i],arr[pos]
        print(arr)

selectionSort([5,3,8,6,7,2])

selectionSort([1,3,8,6,7,2])



