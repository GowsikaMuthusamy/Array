arr=list(map(int,input("ENTER ANY ELEMENTS WITH SPACE:").split()))


def bubblesort(arr):
    n=len(arr)
    for i in range(0,n):
        swappped=False

        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
                
        if not swapped:
            break
        
    return arr
print("Sorted list:", bubblesort(arr))













