class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        i = 0  # Points to last unique element

        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1  # Number of unique elements


# Input and function call
nums = list(map(int, input("Enter sorted array elements separated by space: ").split()))

sol = Solution()
new_length = sol.removeDuplicates(nums)

print("Array after removing duplicates:", nums[:new_length])
print("Number of unique elements:", new_length)
