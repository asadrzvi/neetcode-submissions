class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        for i in range(len(nums)):
            num = 1
            pointer = 0
            while pointer < len(nums):
                if pointer != i:
                    num = num * nums[pointer]
                pointer +=1
            products.append(num)
        return products