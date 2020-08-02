def MergeSort(A):

    if(len(A)>1):

        mid=len(A)//2

        l=A[:mid]
        r=A[mid:]

        print(l)
        print(r)
        print('-----------------------')

        MergeSort(l)
        MergeSort(r)

        i=0
        j=0
        k=0

        while(i<len(l) and j<len(r)):

            if(l[i]<r[j]):

                A[k]=l[i]
                i+=1
                k+=1

            else:

                A[k]=r[j]
                j+=1
                k+=1

        while(i<len(l)):

            A[k]=l[i]
            k+=1
            i+=1

        while(j<len(r)):
            A[k]=r[j]
            k+=1
            j+=1

        # print(l)
        # print(r)
        print(A)

    return A


arr=[15,9,2,3,4]

p=MergeSort(arr)

print(p)