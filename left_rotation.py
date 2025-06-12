#left rotation of an array
nums = list(map(int,input("Enter an elements in an array with space:").split()))
first=nums[0]
for i in range(1,len(nums)):
    nums[i-1]=nums[i]

nums[-1]=first
print("left rotation of an array:",nums)
