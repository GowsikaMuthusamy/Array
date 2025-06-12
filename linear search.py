#linear search
def linear_search(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i
    return -1
try:
    nums = list(map(int,input("enter the array elements with spaces:").split()))
    target = int(input("enter the target element:"))
    result = linear_search(nums,target)
    print("output is:",result)
except ValueError:
    print("enter valid input of numbers")

#left rotation of an array
nums = list(map(int,input("Enter an elements in an array with space:").split()))
first=nums[0]
for i in range(1,len(nums)):
    nums[i-1]=nums[i]

nums[-1]=first
print("left rotation of an array:",nums)

