class Solution:
    def minimumOperations(self, nums):
        operations = 0
        while len(nums) > 0:
            if len(set(nums)) == len(nums):
                return operations
            nums = nums[3:]
            operations += 1
        return operations

        