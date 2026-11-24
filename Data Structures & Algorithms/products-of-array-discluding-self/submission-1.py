class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        check = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            check[i] *= left
            left *= nums[i]
        
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            check[i] *= right
            right *= nums[i]

        return check