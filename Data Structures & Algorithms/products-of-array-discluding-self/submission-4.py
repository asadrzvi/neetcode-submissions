class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        for i in range(len(nums)):
            left = math.prod(nums[:i])
            right = math.prod(nums[i+1:len(nums)])
            products.append(right*left)
        return products