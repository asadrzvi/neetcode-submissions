class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for i in num_set:
            if (i-1) not in num_set:
                current_num = i
                current_length = 1
                while (current_num +1) in num_set:
                    current_num +=1
                    current_length +=1
                longest = max(longest, current_length)
        return longest

