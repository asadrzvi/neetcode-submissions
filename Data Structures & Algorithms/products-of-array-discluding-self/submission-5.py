class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lp = [1]*n
        rp = [1]*n
        results = [1]*n
        
        running_left = 1
        for i in range(n):
            lp[i] = running_left
            running_left *= nums[i]
        
        running_right = 1
        for j in range(n-1, -1, -1):
            rp[j] = running_right
            running_right *= nums[j]

        for i in range(n):
            results[i] = lp[i] * rp[i]

        return results