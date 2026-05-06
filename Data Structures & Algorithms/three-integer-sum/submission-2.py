class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = []
        nums.sort()

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]:
                continue
            j = i+1  
            k = len(nums)-1
            while j < k:
                current_sum = val+nums[j]+nums[k]
                if current_sum > 0:
                    k-=1
                elif current_sum < 0:
                    j+=1
                else:
                    seen.append([val,nums[j],nums[k]])
                    j+=1
                    while nums[j] == nums[j-1] and j < k:
                        j+=1
        return seen