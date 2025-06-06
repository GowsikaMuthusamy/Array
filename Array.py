'''def learn_array():
    arr = [7, 14, 21]
    print("Full array:", arr)
    print("First element:", arr[0])
    print("Second element:", arr[1])
    print("Number of elements:", len(arr))

learn_array()'''


'''def user_array():
    print("enter the elements for array:")
    a=int(input("enter 1 st element:"))
    b=int(input("enter 2 nd element:"))
    c=int(input("enter 3 rd element:"))
    arr=[a,b,c]
    reverse=arr[::-1]
    print(reverse)
user_array()'''

'''def array():
    n=int(input("enter how many elements you want:"))
    arr=[]
    for i in range(n):
        num = int(input(f"enter the element {i+1}:"))
        arr.append(num)
    sums=sum(arr)
    maximum = max(arr)
    print("sum of array:",sums)
    print("maximum element of an array:",maximum)
    print("The arrays are:",arr)
array()'''

def array():
    n=int(input("enter how many elements you want:"))
    arr=[]
    for i in range(n):
        num = int(input(f"enter the element {i+1}:"))
        arr.append(num)
    unique = list(set(arr))
    if len(unique)<2:
        print("-1")
    else:
        sorting = sorted(unique)
        maximum_2 = sorting[-2]
        print("The arrays are:",arr)
        print("sorted array is:",sorting)
        print("the second maximum number in the array is:",maximum_2)  
array()
